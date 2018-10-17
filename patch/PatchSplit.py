# -*- coding: utf-8 -*

import cv2 as cv
import numpy as np
import argparse
import os
import json

"""
# 读取图像，支持 bmp、jpg、png、tiff 等常用格式
IMREAD_UNCHANGED = -1  # 不进行转化，比如保存为了16位的图片，读取出来仍然为16位。
IMREAD_GRAYSCALE = 0  # 进行转化为灰度图，比如保存为了16位的图片，读取出来为8位，类型为CV_8UC1。
IMREAD_COLOR = 1  # 进行转化为RGB三通道图像，图像深度转为8位
IMREAD_ANYDEPTH = 2  # 保持图像深度不变，进行转化为灰度图。
IMREAD_ANYCOLOR = 4  # 若图像通道数小于等于3，则保持原通道数不变；若通道数大于3则只取取前三个通道。图像深度转为8位
"""


def split(patch, overlap, imgPath, outputPath):
    img = cv.imread(imgPath, -1)
    json_data = {}
    key = 0
    json_data["file_name"] = imgPath
    for i in range(0, img.shape[0], patch - overlap):
        for j in range(0, img.shape[1], patch - overlap):
            if patch + i <= img.shape[0] and patch + j <= img.shape[1]:
                img_array = img[i:patch + i, j:patch + j]

                file_name = 'test_' + str(i) + '_' + str(j) + '_patch_' + str(patch) + '_overlap_' + str(
                    overlap) + '_.png'
                save_path = os.path.join(outputPath, file_name)

                cv.imwrite(save_path, img_array, [10, 10])
                json_data[str(key)] = save_path
                key = key+1

    return json_data


def store(data):
    with open('patch.json', 'w') as json_file:
        json_file.write(json.dumps(data))


def load():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="this script can split patch to $PWD or Specified directory")
    parser.add_argument("-i", help="can read file about .tif")
    parser.add_argument("-p", help="patch size ,default=1000", default="1000")
    parser.add_argument("-o", help="output path", default="")
    parser.add_argument("-l", help="overlap size,default=0", default="0")
    args = parser.parse_args()

    data = split(int(args.p), int(args.l), args.i, args.o)
    store(data)
