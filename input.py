#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 1/6/2020 5:28 PM
# @Author  : Jerry
# @Desc    : 
# @File    : input.py
import os


class Input():
    def __init__(self, father_folder_path, file_suffix_list, recursion_flag=False):
        self.father_folder_path = father_folder_path  # 父文件夹路径
        self.file_suffix_list = file_suffix_list  # 需要的文件后缀列表
        self.recursion_flag = recursion_flag  # 是否递归
        self.filepath_list = []

    def get_filepath_list(self):
        '''
        获取待扫描的所有文件的绝对路径(后缀过滤)
        :return:
        '''

        if self.recursion_flag:  # 递归
            for root, dirs, files in os.walk(self.father_folder_path):
                for file in files:
                    if self.__check_file_suffix(file):
                        self.filepath_list.append(os.path.join(root, file))
        else:
            files = os.listdir(self.father_folder_path)
            for file in files:
                if self.__check_file_suffix(file):
                    self.filepath_list.append(os.path.join(self.father_folder_path, file))

        return self.filepath_list

    def __check_file_suffix(self, file_name):
        '''
        检查后缀名
        :param file_name:
        :return:
        '''
        for file_suffix in self.file_suffix_list:
            if file_suffix in file_name:
                return True
        return False
