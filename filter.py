#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 1/6/2020 5:27 PM
# @Author  : Jerry
# @Desc    :
# @File    : filter.py

import re
import os
from xml.etree import ElementTree

from rules import KEYWORDS_LIST, REGEX_DICT


class XmlFilter():
    def __init__(self, xml_path):
        self.xml_path = xml_path
        self.xml_filename = os.path.basename(xml_path)
        self.result_dict = {"keyword": [], "regex": []}

    def __keyword_search(self, item_dict):
        '''
        关键字查找
        :param item_dict: {标签名:值}
        :return:
        '''
        name_list = list(item_dict.keys())
        for key_word in KEYWORDS_LIST:
            match = re.search(key_word, name_list[0], re.IGNORECASE)
            if match:
                if item_dict not in self.result_dict['keyword']:
                    self.result_dict['keyword'].append(item_dict)

    def __regex_search(self, item_dict):
        '''
        正则表达式匹配
        :param item_dict: {标签名:值}
        :return:
        '''
        value_list = list(item_dict.values())
        if value_list[0]:  # 处理这种情况{'t2': None}
            for regex_name, regex_patern in REGEX_DICT.items():
                match = re.search(regex_patern, value_list[0])
                if match:
                    if item_dict not in self.result_dict['regex']:
                        self.result_dict['regex'].append(item_dict)

    def filtering(self):
        # refs:https://www.cnblogs.com/ifantastic/archive/2013/04/12/3017110.html
        root = ElementTree.parse(self.xml_path)
        for node in root.iter():
            node_attrib_list = (list((node.attrib.items())))
            if node_attrib_list:
                attrib_value = (node_attrib_list[0][1])
                value_attrib_value = (node.get('value', default=None))
                if value_attrib_value:
                    item_dict = {attrib_value: value_attrib_value}  # 情况:  <long name="aaa" value="xxx" />
                else:
                    item_dict = {attrib_value: node.text}  # 情况: <string name="aaa">bbb</string>
                self.__keyword_search(item_dict)
                self.__regex_search(item_dict)
        return self.result_dict
