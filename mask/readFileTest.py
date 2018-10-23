#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
from skimage import io
from ProcessingTest import read_heat_map
import argparse


def read_file(file_path, file_list, file_name_list, extention="png"):
    if os.path.isfile(file_path):
        file_name, ext = get_file_extention(file_path)
        if ext == extention:
            file_list.append(file_path)
            file_name_list.append(file_name)
    else:
        for i in os.listdir(file_path):
            new_path = os.path.join(file_path, i)
            read_file(new_path, file_list, file_name_list, extention)


def get_file_extention(file_path):
    file_name = os.path.split(file_path)
    file_format = os.path.splitext(file_name[1])
    return file_format[0], file_format[-1][1:]


if __name__ == "__main__":
    file_list = []
    file_name_list = []
    parser = argparse.ArgumentParser(description="this script can read dir to find file ")
    parser.add_argument("-i", help="write file full path", default="./")
    parser.add_argument("-o", help="heatmap output file path", default="./heatmap")
    parser.add_argument("-m", help="mask output file path", default="./mask")
    args = parser.parse_args()

    read_file(args.i, file_list, file_name_list)
    for i in range(len(file_list)):

        if(os.path.exists(args.o) == False):
            os.mkdir(args.o)
        if(os.path.exists(args.m) == False):
            os.mkdir(args.m)

        heatmap_out = os.path.join(args.o, file_name_list[i] + "_0309.png")
        mask_out = os.path.join(args.m, file_name_list[i] + "_mask.png")
        base_arr, mask_fin = read_heat_map(file_list[i])

        io.imsave(heatmap_out, base_arr)
        io.imsave(mask_out, mask_fin)
