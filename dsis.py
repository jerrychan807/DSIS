#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 1/7/2020 11:08 AM
# @Author  : Jerry
# @Desc    : 
# @File    : dsis.py

from sys import argv

from input import Input
from filter import XmlFilter
from output import Output

father_folder_path = argv[1]
file_suffix_list = ['.xml']
inputer = Input(father_folder_path=father_folder_path, recursion_flag=True, file_suffix_list=file_suffix_list)
filepath_list = inputer.get_filepath_list()

for filepath in filepath_list:
    print(filepath)
    filter = XmlFilter(filepath)
    filter.filtering()
    output = Output(filter.xml_filename, filter.result_dict)
    output.draw_table()
    if filter.result_dict:
        print(output.table)
