#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 16:11  
# @Author  : Siman Guo
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : ranzhi_suite.py  
# @Software: PyCharm Community Edition

import unittest
from test_case.test_ranzhi_login import testRanZhiLogin


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(testRanZhiLogin))

    return suite
