#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 1/6/2020 5:29 PM
# @Author  : Jerry
# @Desc    : 
# @File    : output.py

from prettytable import PrettyTable


class Output():
    def __init__(self, xml_filename, result_dict):
        self.xml_filename = xml_filename
        self.result_dict = result_dict
        self.table = PrettyTable(['FileName', 'Method', 'AttribName', 'AttribValue'])

    def draw_table(self):
        for method, value in self.result_dict.items():
            for attri_item in self.result_dict[method]:
                self.table.add_row(
                    [self.xml_filename, method, list(attri_item.keys())[0], list(attri_item.values())[0]])
