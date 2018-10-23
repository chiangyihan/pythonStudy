#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from skimage import io
import numpy as np
from ProcessingTest import read_img_normalization, img_binarization, read_heat_map
from PIL import Image, ImageFont, ImageDraw
import argparse
import os


def img_read(mask_03, mask_06, mask_09, output_path):
    h, w = mask_03.shape
    img_RGB = np.zeros((h, w, 3), dtype=np.uint16)
    img_RGB[:, :, 0] = mask_03
    img_RGB[:, :, 1] = mask_06
    img_RGB[:, :, 2] = mask_09

    img_draw(np.asarray(img_RGB, dtype=np.uint8), output_path)


def img_draw(img_arr, output_path):
    h, w, a = img_arr.shape
    image = Image.fromarray(img_arr)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/malayalam/Suruma.ttf', 16, encoding="unic")  # 设置字体
    draw_content = [[u'0.3,0.6,0.9', "#ffffff"], [u'0.3', "#ff0000"], [u'0.6', "#00ff00"],
                    [u'0.9', "#0000ff"], [u'0.3,0.6', "#ffff00"], [u'0.6,0.9', "#00ffff"],
                    [u'0.3,0.9', "#ff00ff"]]
    for i in range(len(draw_content)):
        draw.text((w - 80, 20 * i), draw_content[i][0], draw_content[i][1], font)
    # image.show()
    image_arr = np.asarray(image, dtype=np.uint16)
    io.imsave(output_path, image_arr)


# 拼接文件名,文件名为:源文件名_modify.源文件格式
def name_join(input_path, output_path, name_modify):
    file_path = os.path.split(input_path)
    file_name = os.path.splitext(file_path[1])
    end_name = os.path.join(output_path, file_name[0] + "_" + name_modify + file_name[1])
    return end_name


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this script can read heatmap file, write three different mask," + \
                                                 "and make an RGB image")
    parser.add_argument("-i", help="write file full path", default="./mask.png")
    parser.add_argument("-o", help="write output file path", default="./")
    args = parser.parse_args()

    img_arr, img_prob = read_img_normalization(args.i)
    base_arr, mask_fin = read_heat_map(args.i)
    mask_03 = img_binarization(img_arr, 0.3)
    mask_09 = img_binarization(img_arr, 0.9)

    rgb_name = name_join(args.i,args.o,"RGB")
    img_read(mask_03, mask_fin, mask_09, rgb_name)
