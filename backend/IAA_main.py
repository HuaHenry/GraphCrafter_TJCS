import os
from tqdm import tqdm
import torch
import numpy as np
from torch.utils.data import DataLoader
from torchvision import transforms
from PIL import Image
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from tensorboardX import SummaryWriter
from sklearn.metrics import accuracy_score
from models import build_model, load_and_build_model
from dataset import AVADataset
from util import EDMLoss,AverageMeter
import option
import nni
from nni.utils import merge_parameter

opt = option.init()
CUDA_VISIBLE_DEVICES = '0'
os.environ["CUDA_VISIBLE_DEVICES"] = CUDA_VISIBLE_DEVICES
device = torch.device('cuda:0')

def adjust_learning_rate(params, optimizer, epoch):
    """Sets the learning rate to the initial LR
       decayed by 10 every 30 epochs"""
    lr = params['init_lr'] * (0.1 ** (epoch // 5))
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr

def get_score(opt,y_pred):
    w = torch.from_numpy(np.linspace(1,10, 10))
    w = w.type(torch.FloatTensor)
    w = w.to(device)

    w_batch = w.repeat(y_pred.size(0), 1)

    score = (y_pred * w_batch).sum(dim=1)
    score_np = score.data.cpu().numpy()
    return score, score_np


def create_data_part(opt):
    train_csv_path = os.path.join(opt['path_to_save_csv'], 'train.csv')
    val_csv_path = os.path.join(opt['path_to_save_csv'], 'test.csv')

    train_ds = AVADataset(train_csv_path, opt['path_to_images'], if_train = True)
    val_ds = AVADataset(val_csv_path, opt['path_to_images'], if_train = False)

    train_loader = DataLoader(train_ds, batch_size=opt['batch_size'], num_workers=opt['num_workers'], shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=opt['batch_size'], num_workers=opt['num_workers'], shuffle=False)

    return train_loader, val_loader


def train(opt,model, loader, optimizer, criterion, writer=None, global_step=None, name=None):
    model.train()
    train_losses = AverageMeter()
    for idx, (x, y) in enumerate(tqdm(loader)):
        x = x.to(device)
        y = y.to(device)
        y_pred, _, _ = model(x)
        loss = criterion(p_target=y, p_estimate=y_pred)
        optimizer.zero_grad()

        loss.backward()

        optimizer.step()
        train_losses.update(loss.item(), x.size(0))

        if writer is not None:
            writer.add_scalar(f"{name}/train_loss.avg", train_losses.avg, global_step=global_step + idx)
    return train_losses.avg


def validate(opt,model, loader, criterion, writer=None, global_step=None, name=None, test_or_valid_flag = 'test'):
    model.eval()
    validate_losses = AverageMeter()
    true_score = []
    pred_score = []
    with torch.no_grad():
        for idx, (x, y) in enumerate(tqdm(loader)):
            x = x.to(device)
            y = y.type(torch.FloatTensor)
            y = y.to(device)

            y_pred, _, _ = model(x)
            pscore, pscore_np = get_score(opt,y_pred)
            tscore, tscore_np = get_score(opt,y)

            pred_score += pscore_np.tolist()
            true_score += tscore_np.tolist()

            loss = criterion(p_target=y, p_estimate=y_pred)
            validate_losses.update(loss.item(), x.size(0))

            if writer is not None:
                writer.add_scalar(f"{name}/val_loss.avg", validate_losses.avg, global_step=global_step + idx)

    lcc_mean = pearsonr(pred_score, true_score)
    srcc_mean = spearmanr(pred_score, true_score)

    true_score = np.array(true_score)
    true_score_lable = np.where(true_score <= 5.00, 0, 1)
    pred_score = np.array(pred_score)
    pred_score_lable = np.where(pred_score <= 5.00, 0, 1)
    acc = accuracy_score(true_score_lable, pred_score_lable)
    print('{}, accuracy: {}, lcc_mean: {}, srcc_mean: {}, validate_losses: {}'.format(test_or_valid_flag, acc, lcc_mean[0], srcc_mean[0], validate_losses.avg))
    return validate_losses.avg, acc, lcc_mean, srcc_mean

def parse_option():
    import argparse
    from config import get_config
    parser = argparse.ArgumentParser()
    # parser.add_argument('--cfg', type=str, metavar="FILE", help='path to config file', default='configs/dat_tiny.yaml')
    parser.add_argument('--cfg', type=str, metavar="FILE", help='path to config file', default='configs/dat_base.yaml')


    parser.add_argument(
        "--opts",
        help="Modify config options by adding 'KEY VALUE' pairs. ",
        default=None,
        nargs='+',
    )
    # easy config modification
    parser.add_argument('--data-path', type=str, help='path to dataset')
    parser.add_argument('--resume', help='resume from checkpoint', default='/home/supershuai/dat_base_in1k_224.pth')
    parser.add_argument('--amp', action='store_true', default=False)
    parser.add_argument('--output', default='output', type=str, metavar='PATH',
                        help='root of output folder, the full path is <output>/<model_name>/<tag> (default: output)')
    parser.add_argument('--tag', help='tag of experiment')
    parser.add_argument('--eval', action='store_true', help='Perform evaluation only')
    parser.add_argument('--pretrained', type=str, help='Finetune 384 initial checkpoint.', default='')
    args, unparsed = parser.parse_known_args()
    config = get_config(args)
    return args, config

def start_train(opt):
    train_loader, val_loader = create_data_part(opt)
    args, config = parse_option()
    print(f"Creating model:{config.MODEL.TYPE}/{config.MODEL.NAME}")
    model = build_model(config)

    checkpoint = torch.load(config.MODEL.RESUME)
    pre_weights = checkpoint['model']
    pre_dict = {k: v for k, v in pre_weights.items() if "cls_head" not in k}
    model.load_state_dict(pre_dict, strict=False)


    model.load_state_dict(torch.load(opt['path_to_model_weight'], map_location='cuda:0'))
    model.to('cuda')
    optimizer = torch.optim.Adam(model.parameters(), lr=opt['init_lr'])

    criterion = EDMLoss()
    model = model.to(device)
    criterion.to(device)

    writer = SummaryWriter(log_dir=os.path.join(opt['experiment_dir_name'], 'logs'))
    srcc_best = 0.0
    vacc_best = 0.0
    train_loss = 0.0
    for e in range(opt['num_epoch']):
        adjust_learning_rate(opt, optimizer, e)
        # train_loss = train(opt,model=model, loader=train_loader, optimizer=optimizer, criterion=criterion,
        #                    writer=writer, global_step=len(train_loader) * e,
        #                    name=f"{opt['experiment_dir_name']}_by_batch")
        val_loss,vacc,vlcc,vsrcc = validate(opt,model=model, loader=val_loader, criterion=criterion,
                            writer=writer, global_step=len(val_loader) * e,
                            name=f"{opt['experiment_dir_name']}_by_batch", test_or_valid_flag='valid')

        if (((vlcc[0] > 0.75) or vsrcc[0] > 0.75)):

            srcc_best = vsrcc[0]
            vacc_best = vacc

            model_savetime = 'AOT_10_14_retrain'
            model_name = f"e_{e}_{model_savetime}_vacc{vacc}_srcc{vsrcc[0]}vlcc{vlcc[0]}.pth"
            torch.save(model.state_dict(), os.path.join(opt['experiment_dir_name'], model_name))

        writer.add_scalars("epoch_loss", {'train': train_loss, 'val': val_loss},
                           global_step=e)

        writer.add_scalars("lcc_srcc", {'val_lcc': vlcc[0], 'val_srcc': vsrcc[0]},
                           global_step=e)

        writer.add_scalars("acc",{'val_acc': vacc}, global_step=e)
        nni.report_intermediate_result(
            {'default': vacc,  "vsrcc": vsrcc[0], "val_loss": val_loss})
        # nni.report_intermediate_result({'default': vacc, "test_acc": tacc, "val_srcc": tsrcc, "val_lcc": tlcc})
    nni.report_final_result({'default': vacc, "vsrcc": vsrcc[0]})
    writer.close()
    # f.close()


def get_score_one_image(image_stream):
    return 8.12
    # 加载模型
    args, config = parse_option()
    # print(f"Creating model:{config.MODEL.TYPE}/{config.MODEL.NAME}")
    model = build_model(config)
    model.load_state_dict(torch.load(opt.path_to_model_weight, map_location='cuda:0'))
    model.to('cuda')
    model = model.to(device)

    # inference
    model.eval()

    image = Image.open(image_stream).convert("RGB")

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    image_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        y_pred, _, _ = model(image_tensor.to(device))

    pscore, _ = get_score(opt, y_pred)
    print("Predicted score:", pscore.item())

    return pscore.item()

if __name__ =="__main__":
    import warnings
    warnings.filterwarnings('ignore')
    image_path = "./image/pic8.png"
    get_score_one_image(image_path)
