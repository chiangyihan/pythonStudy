#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import nibabel as nib
import skimage.io as io
import skimage.measure
import skimage.draw
import numpy as np


# 用于读取nii文件，原始文件，输出标注后图片
def nii_read_and_save(nii_path, base_path, output_path):
    base_img = io.imread(base_path)
    img = nib.load(nii_path)
    img_arr = img.get_fdata()
    img_arr = np.squeeze(img_arr)

    # 用于将灰度图片转换为rgb图片
    if len(base_img.shape) == 2:
        h, w = base_img.shape
        rgb_img = np.zeros((h, w, 3))
        rgb_img[:, :, 0] = base_img
        rgb_img[:, :, 1] = base_img
        rgb_img[:, :, 2] = base_img
    else:
        rgb_img = base_img

    # 转置矩阵，描边
    contours = skimage.measure.find_contours(img_arr.T, 0.5)

    # 画线
    contours_len = len(contours[0]) - 1
    for i in range(0, contours_len):
        x_point = contours[0][i][0].astype(int)
        y_point = contours[0][i][1].astype(int)
        next_x_point = contours[0][i + 1][0].astype(int)
        next_y_point = contours[0][i + 1][1].astype(int)
        rr, cc = skimage.draw.line(x_point, y_point, next_x_point, next_y_point)
        skimage.draw.set_color(rgb_img, [rr, cc], [255, 255, 0])

        if i == contours_len:
            x_point = contours[0][i][0].astype(int)
            y_point = contours[0][i][1].astype(int)
            next_x_point = contours[0][0][0].astype(int)
            next_y_point = contours[0][0][1].astype(int)
            rr, cc = skimage.draw.line(x_point, y_point, next_x_point, next_y_point)
            skimage.draw.set_color(rgb_img, [rr, cc], [255, 255, 0])

    io.imsave(output_path, rgb_img.astype(int))


if __name__ == "__main__":
    nii_path = "/home/qiang/nii/CengXiaoNan_R_CC_Merge.nii"
    base_path = "/home/qiang/nii/test1.png"
    base_path = "/home/qiang/nii/1_NORMAL.pnm"
    nii_read_and_save(nii_path, base_path, output_path)

