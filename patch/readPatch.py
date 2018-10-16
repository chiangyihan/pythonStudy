#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json
import cv2 as cv
import os
import argparse


def load(data_json):
    with open(data_json) as json_file:
        data = json.load(json_file)
        return data


def write_show(patch_list, imgPath, outputPath, x_list, y_list):
    show_img = cv.imread(imgPath, -1)
    length = len(x_list)
    for i in range(0, length):
        x = x_list[i]
        y = y_list[i]
        patch = patch_list[i]
        show_img[x:x + 1, y:y + patch] = 255
        show_img[x:x + patch, y:y + 1] = 255
        show_img[x + patch:x + patch + 1, y:y + patch] = 255
        show_img[x:x + patch, y + patch:y + patch + 1] = 255
        save_path_show = os.path.join(outputPath, "show.png")
    cv.imwrite(save_path_show, show_img, [10, 10])


def read_json_file(input_path, output_path):
    read_json = load(input_path)
    file_path = read_json["file_name"]
    x = []
    y = []
    patch = []
    overlap = []

    for i in range(0, len(read_json) - 1):
        a = read_json[str(i)]
        read_split = str(a).split("_")
        x.append(int(read_split[1]))
        y.append(int(read_split[2]))
        patch.append(int(read_split[4]))
        overlap.append(int(read_split[6]))

    write_show(patch, file_path, output_path, x, y)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this script can read json file by PatchSplit")
    parser.add_argument("-i", help="write json file full path", default="patch.json")
    parser.add_argument("-o", help="write output file path", default="")
    args = parser.parse_args()

    read_json_file(args.i, args.o)
