import cv2 as cv
import numpy as np

from simple_image_process.utils import plt_save


def show_hsv(src, type,size):
    width = size[0]
    height = size[1]

    # 转换成HSV色彩空间
    hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)

    if type == "Hue":
        # 色度/色调
        plt_save(image=h, title='Hue',width_pixels=width,height_pixels=height)
    elif type == "Saturation":
        # 饱和度
        plt_save(image=s, title='Saturation',width_pixels=width,height_pixels=height)
    elif type == "Value":
        # 纯度/亮度
        plt_save(image=v, title='Value',width_pixels=width,height_pixels=height)
    elif type == "Fixed Hue":
        # 固定色度h
        h_new = np.full_like(h, 255)
        merge = cv.merge([h_new, s, v])
        plt_save(merge, 'Fixed Hue',width_pixels=width,height_pixels=height)
    elif type == "Fixed Saturation":
        # 固定饱和度s
        s_new = np.full_like(s, 255)
        merge = cv.merge([h, s_new, v])
        plt_save(merge, 'Fixed Saturation',width_pixels=width,height_pixels=height)
    elif type == "Fixed Value":
        # 固定亮度v
        v_new = np.full_like(v, 255)
        merge = cv.merge([h, s, v_new])
        plt_save(merge, 'Fixed Value',width,height)
    elif type == "Fixed Hue & Saturation":
        # 固定色度h + 固定饱和度s
        h_new = np.full_like(h, 255)
        s_new = np.full_like(s, 255)
        merge = cv.merge([h_new, s_new, v])
        plt_save(merge, 'Fixed Hue & Saturation',width,height)
    elif type == "Fixed Hue & Value":
        # 固定色度h + 固定亮度v
        h_new = np.full_like(h, 255)
        v_new = np.full_like(v, 255)
        merge = cv.merge([h_new, s, v_new])
        plt_save(merge, 'Fixed Hue & Value',width,height)
    elif type == "Fixed Saturation & Value":
        # 固定饱和度s + 固定亮度v
        s_new = np.full_like(s, 255)
        v_new = np.full_like(v, 255)
        merge = cv.merge([h, s_new, v_new])
        plt_save(merge, 'Fixed Saturation & Value',width,height)
