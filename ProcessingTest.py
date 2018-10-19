#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from skimage import io, measure
import numpy as np
import argparse
import os


def read_heat_map(input_path,alpha=0.5):
    img_arr, img_rate = read_img_normalization(input_path)
    mask_low = img_binarization(img_arr, 0.3)
    mask_high = img_binarization(img_arr, 0.9)

    base_arr = np.zeros_like(img_arr, dtype=np.uint16)

    label_low = measure.label(mask_low)
    props_low = measure.regionprops(label_low)

    for i in range(len(props_low)):
        len_coords = len(props_low[i].coords)
        base_tmp = np.zeros_like(base_arr, dtype=np.uint16)
        if len_coords > 1:
            count_low = 0
            count_high = 0
            for j in range(len_coords):
                props_low_h = props_low[i].coords[j][0]
                props_low_w = props_low[i].coords[j][1]
                count_low += mask_low[props_low_h, props_low_w]
                count_high += mask_high[props_low_h, props_low_w]
                base_tmp[props_low_h, props_low_w] = img_rate[props_low_h, props_low_w]
            a_real = float(count_high) / count_low
            if a_real >= alpha:
                base_arr = base_arr + base_tmp
    mask_06 = img_binarization(base_arr, 0.6)
    return base_arr, mask_06


# 读取图片，返回归一化图片与原图片
def read_img_normalization(input_path):
    img_read = io.imread(input_path, as_gray=True)
    if img_read.dtype == np.uint16:
        img_normal = img_read / 65535.0
    elif img_read.dtype == np.uint8:
        img_normal = img_read / 255.0
    else:
        print("this type can not read", img_arr.dtype)
    return img_normal, img_read


# 二值化
def img_binarization(img_gray, threshold, max_val=255, img_type=np.uint8):
    return np.asarray((img_gray > threshold) * max_val).astype(img_type)


if __name__ == "__main__":
    base_arr, mask_06 = read_heat_map("/home/qiang/pic/mask.png")
    io.imsave("/home/qiang/pic/base_arr.png",base_arr)
    io.imsave("/home/qiang/pic/mask_06.png",mask_06)
