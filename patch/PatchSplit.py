# -*- coding: utf-8 -*

import cv2 as cv
import numpy as np
import argparse

"""
# 读取图像，支持 bmp、jpg、png、tiff 等常用格式
IMREAD_UNCHANGED = -1  # 不进行转化，比如保存为了16位的图片，读取出来仍然为16位。
IMREAD_GRAYSCALE = 0  # 进行转化为灰度图，比如保存为了16位的图片，读取出来为8位，类型为CV_8UC1。
IMREAD_COLOR = 1  # 进行转化为RGB三通道图像，图像深度转为8位
IMREAD_ANYDEPTH = 2  # 保持图像深度不变，进行转化为灰度图。
IMREAD_ANYCOLOR = 4  # 若图像通道数小于等于3，则保持原通道数不变；若通道数大于3则只取取前三个通道。图像深度转为8位
"""


def split(patch, overlap, img):
    show_img = img.copy()
    for i in range(0, img.shape[0], patch - overlap):
        for j in range(0, img.shape[1], patch - overlap):
            if patch - overlap + i <= img.shape[0] and patch - overlap + j <= img.shape[1]:
                img_array = img[i:patch + i, j:patch + j]
                show_img[i:i + 10, j:j + patch] = 255
                show_img[i:i + patch, j:j + 10] = 255
                show_img[i + patch:i + patch + 10, j:j + patch] = 255
                show_img[i:i + patch, j + patch:j + patch + 10] = 255
                print
                'test' + '_' + str(i) + '_' + str(j) + '_patch_' + str(patch) + '_overlap_' + str(overlap) + '.png'
                cv.imwrite(
                    'test' + '_' + str(i) + '_' + str(j) + '_patch_' + str(patch) + '_overlap_' + str(overlap) + '.png',
                    img_array, [10, 10])
    cv.imwrite('show.png', show_img, [10, 10])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="this script can split patch to $PWD")
    parser.add_argument("-r", help="can read file about .tif")
    parser.add_argument("-p", help="patch size", default="1000")
    parser.add_argument("-o", help="overlap size", default="0")
    args = parser.parse_args()

    img = cv.imread(args.r, -1)
    # img = cv.imread("/home/qiang/pic/CRC-Prim-HE-07_APPLICATION.tif", -1)
    split(int(args.p), int(args.o), img)
