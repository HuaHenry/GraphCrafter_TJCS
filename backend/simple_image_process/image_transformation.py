import cv2
import numpy as np

from simple_image_process.utils import plt_save


def show_transformation(src,type,size):
    width = size[0]
    height = size[1]

    # 用形态学滤波器腐蚀和膨胀图像
    element_3x3 = np.ones((3, 3), np.uint8)
    image_gray = cv2.cvtColor(src=src, code=cv2.COLOR_RGB2GRAY)
    element_5x5 = np.ones((5, 5), np.uint8)
    element_7x7 = np.ones((7, 7), np.uint8)

    # 腐蚀 3x3
    if type == 'eroded':
        eroded = cv2.erode(src=src, kernel=element_3x3)
        plt_save(image=eroded, title='eroded',width_pixels=width,height_pixels=height)

    elif type == 'dilated 3 times':
        # 膨胀 3x3 3次
        dilated = cv2.dilate(src=src, kernel=element_3x3, iterations=3)
        plt_save(image=dilated, title='dilated 3 times',width_pixels=width,height_pixels=height)

    elif type == 'eroded 7x7':
        # 腐蚀 7x7
        eroded_7x7 = cv2.erode(src=src, kernel=element_7x7, iterations=1)
        plt_save(image=eroded_7x7, title='eroded 7x7',width_pixels=width,height_pixels=height)

    elif type == 'eroded 3 times':
        # 腐蚀 3x3 3次
        eroded_3 = cv2.erode(src=src, kernel=element_3x3, iterations=3)
        plt_save(image=eroded_3, title='eroded 3 times',width_pixels=width,height_pixels=height)

    elif type == 'closed':
        # 用形态学滤波器开启和闭合图像
        image_gray = cv2.cvtColor(src=src, code=cv2.COLOR_RGB2GRAY)
        closed = cv2.morphologyEx(src=image_gray, op=cv2.MORPH_CLOSE, kernel=element_5x5)
        plt_save(image=closed, title='closed',width_pixels=width,height_pixels=height)

    elif type == 'opened':
        # Open the image
        opened = cv2.morphologyEx(src=image_gray, op=cv2.MORPH_OPEN, kernel=element_5x5)
        plt_save(image=opened, title='opened',width_pixels=width,height_pixels=height)

    elif type == 'Closed 2 Opened':
        closed = cv2.morphologyEx(src=image_gray, op=cv2.MORPH_CLOSE, kernel=element_5x5)
        closed_opened = cv2.morphologyEx(src=closed, op=cv2.MORPH_OPEN, kernel=element_5x5)
        plt_save(image=closed_opened, title='Closed 2 Opened',width_pixels=width,height_pixels=height)

    elif type == 'Opened 2 Closed':
        opened = cv2.morphologyEx(src=image_gray, op=cv2.MORPH_OPEN, kernel=element_5x5)
        opened_closed = cv2.morphologyEx(src=opened, op=cv2.MORPH_CLOSE, kernel=element_5x5)
        plt_save(image=opened_closed, title='Opened 2 Closed',width_pixels=width,height_pixels=height)

    elif type == 'Gradient or Edge':
        # 在灰度图像中应用形态学运算
        edge = cv2.morphologyEx(src=image_gray, op=cv2.MORPH_GRADIENT, kernel=element_3x3)
        plt_save(image=255 - edge, title='Gradient or Edge',width_pixels=width,height_pixels=height)

    elif type == 'Gradient or Edge 2 Thresh Binary or Edge':
        edge = cv2.morphologyEx(src=image_gray, op=cv2.MORPH_GRADIENT, kernel=element_3x3)
        threshold = 80
        _, thresh_binary = cv2.threshold(src=edge, thresh=threshold, maxval=255, type=cv2.THRESH_BINARY)
        plt_save(image=thresh_binary, title='Gradient or Edge 2 Thresh Binary or Edge',width_pixels=width,height_pixels=height)

    elif type == '7x7 Black Top-hat':
        black_hat = cv2.morphologyEx(src=image_gray, op=cv2.MORPH_BLACKHAT, kernel=element_7x7)
        plt_save(image=255 - black_hat, title='7x7 Black Top-hat',width_pixels=width,height_pixels=height)

    elif type == '7x7 Black Top-hat 2 Thresh Binary or Edge':
        black_hat = cv2.morphologyEx(src=image_gray, op=cv2.MORPH_BLACKHAT, kernel=element_7x7)
        threshold = 25
        _, thresh_binary = cv2.threshold(src=black_hat, thresh=threshold, maxval=255, type=cv2.THRESH_BINARY)
        plt_save(image=255 - thresh_binary, title='7x7 Black Top-hat 2 Thresh Binary or Edge',width_pixels=width,height_pixels=height)

    elif type == '7x7 Black Top-hat 2 Closed':
        threshold = 25
        black_hat = cv2.morphologyEx(src=image_gray, op=cv2.MORPH_BLACKHAT, kernel=element_7x7)
        _, thresh_binary = cv2.threshold(src=black_hat, thresh=threshold, maxval=255, type=cv2.THRESH_BINARY)
        closed = cv2.morphologyEx(src=thresh_binary, op=cv2.MORPH_CLOSE, kernel=element_7x7)
        plt_save(image=255 - closed, title='7x7 Black Top-hat 2 Closed',width_pixels=width,height_pixels=height)
