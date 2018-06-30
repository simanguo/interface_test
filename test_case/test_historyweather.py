#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 15:51  
# @Author  : Siman Guo
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : test_historyweather.py  
# @Software: PyCharm Community Edition

import requests
from config import config
import unittest


class testHistoryWeather(unittest.TestCase):

    def setUp(self):
        self.key = config.appkey
        self.province_url = config.host + "province"
        self.city_url = config.host + "citys"
        self.hisweather_url = config.host + "weather"
        self.province_id = 1

    def tearDown(self):
        pass

    def test_1get_province(self):
        param = "key=" + self.key
        res = requests.get(self.province_url, param)
        jsonRes = res.json()
        self.assertEqual(jsonRes.get("reason"), "查询成功")
        # result = jsonRes.get("result")
        # for i in range(len(result)):
        #     province = result[i].get('province')
        #     if "广东" == province:
        #         self.province_id = result[i].get("id")

    def test_2get_citylist(self):
        payload = {"key": self.key,
                   "province_id": 1}
        res = requests.post(self.city_url, data=payload)
        jsonres = res.json()
        self.assertEqual(jsonres.get("reason"), "查询成功")

    def test_3get_historyweather(self):
        payload = {"key": self.key,
                   "city_id": 1,
                   "weather_date": "2018-06-22"}
        res = requests.post(self.hisweather_url, data=payload)
        jsonres = res.json()
        self.assertEqual(jsonres.get("reason"), "查询成功")


if __name__ == "__main__":
    unittest.main()
