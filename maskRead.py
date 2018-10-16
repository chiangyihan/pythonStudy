#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np


def normalization(mask_path, output_path):
    img_arr = cv.imread(mask_path)
    i_max, i_min = img_arr.max(), img_arr.min()
    img_arr = (img_arr - i_min) / (i_max - i_min)
    threshold, binaryzation_matrix = cv.threshold(img_arr, 0.9, 255, cv.THRESH_BINARY)

    fil = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]])

    cv.imwrite(output_path, binaryzation_matrix)

    res = cv.filter2D(binaryzation_matrix, -1, fil)

    cv.imwrite("/home/qiang/pic/res.png", res)


if __name__ == "__main__":
    normalization("/home/qiang/pic/mask.png", "/home/qiang/pic/output.png")
