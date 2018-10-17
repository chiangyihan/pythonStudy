#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from skimage import io
import numpy as np
import argparse


def isolated_remove(input_path, output_path, size=1):
    img_arr = io.imread(input_path, as_gray=True)

    if img_arr.dtype == np.uint16:
        img_arr = img_arr / 65535.0
    elif img_arr.dtype == np.uint8:
        img_arr = img_arr / 255.0
    else:
        print("this type can not read", img_arr.dtype)

    mask = img_binaryzation(img_arr, 0.9)

    fil = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]])

    h, w = mask.shape
    new_mask = mask.copy()
    for i in range(1, h):
        for j in range(1, w):
            if i + size < h and j + size < w:
                img_tmp = new_mask[i - size:i + size + 1, j - size:j + size + 1]
                img_tmp = np.multiply(img_tmp, fil)
                k = np.sum(img_tmp)
                if k == 0:
                    mask[i, j] = 0
    io.imsave(output_path, mask)


# 用于进行二值化，默认uint8类型，最大值为255。输入参数依次为numpy格式灰度图片，阈值，最大值，类型
def img_binaryzation(img_gray, threshold, max_val=255, img_type=np.uint8):
    return np.asarray((img_gray > threshold) * max_val).astype(img_type)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this script can read image ,remove isolated")
    parser.add_argument("-i",help="write input file's absolute path, default is $PWD 'mask.png' ", default="mask.png")
    parser.add_argument("-o",help="write output file's absolute path, default is $PWD 'output.png'", default="./output.png")
    args = parser.parse_args()
    isolated_remove(args.i, args.o)
