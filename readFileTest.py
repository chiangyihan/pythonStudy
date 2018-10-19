#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os


def read_file(file_path, file_list, extention="dcm"):
    if os.path.isfile(file_path):
        ext = get_file_extention(file_path)
        if ext == extention:
            file_list.append(file_path)
    else:
        for i in os.listdir(file_path):
            new_path = os.path.join(file_path, i)
            read_file(new_path, file_list, extention)


def get_file_extention(file_path):
    file_abname = os.path.split(file_path)
    return file_abname[1]


if __name__ == "__main__":
    file_list = []
    # read_file("/home/qiang/dcm", file_list)

    print(file_list)
