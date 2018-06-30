#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 16:35  
# @Author  : Siman Guo
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : weather_suite.py  
# @Software: PyCharm Community Edition

import unittest
from test_case.test_historyweather import testHistoryWeather

def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    testcases = loader.loadTestsFromTestCase(testHistoryWeather)
    suite.addTests(testcases)

    return suite
