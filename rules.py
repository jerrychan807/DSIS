#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 1/6/2020 5:32 PM
# @Author  : Jerry
# @Desc    :
# @File    : rules.py

KEYWORDS_LIST = ['api', 'key',
                 'username', 'user', 'uname',
                 'pw', 'password', 'pass', 'passwd', 'pwd'
                 # 'email', 'mail',
                                                     'credentials', 'credential', 'cred', 'login',
                 'ip', 'host', 'domain', 'url', 'proxy', 'port', 'auth',
                 'token', 'secret']

REGEX_DICT = {
    "PHONE_REGEX": r'^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7(?:[35678]\d{2}|4(?:0\d|1[0-2]|9\d))|9[189]\d{2}|66\d{2})\d{6}$',
    "EMAIL_REGEX": r'^\w+@(\w+\.)+\w+',
    "IDCARD_REGEX": r'^[1-9]\d{5}(18|19|20)\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]'
}
