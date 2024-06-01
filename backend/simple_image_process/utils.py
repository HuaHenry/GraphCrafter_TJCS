import matplotlib.pyplot as plt


def plt_save(image, title='', width_pixels=480, height_pixels=480, dpi=100):
    width_inches = width_pixels / dpi
    height_inches = height_pixels / dpi

    plt.ioff()
    plt.figure(figsize=(width_inches, height_inches))
    plt.axis('off')
    plt.imshow(X=image, cmap='gray')

    file_path = './img_tmp/tmp.png'
    plt.savefig(file_path, bbox_inches='tight', pad_inches=0) # 消除白边
    print(file_path)


def plt_show(image, title=''):
    plt.imshow(X=image, cmap='gray')
    plt.title(title)
    plt.show()
