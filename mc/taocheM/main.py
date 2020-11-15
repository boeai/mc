# -*- coding:utf-8 -*-
import unittest
from service import AutoTest
from taocheM.config_m import config
#from taocheM.test_home.test_Hotsearch import Hotsearch
from taocheM.test_buycar.test_SearchBM import searchbm
from taocheM.test_home.test_CarBrand import CarBrand
from taocheM.test_home.test_Newcar import Newcar
from taocheM.test_sellcar.test_sellcar import SellCar

to_user = config.to_user

# 环境标识
env = config.env


# 当前目录
test_dir = "./test_crawler/test_m_crawler/"
# 自动加载test_dir下所有以test开头的文件中以test开头的测试方法
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
runner = AutoTest(suite=discover, name='用例调试', to_user=to_user, case_type='M', env=env)
runner.run()


# suite = unittest.TestSuite()
# suite.addTest(CarBrand('test_CarBrand'))
#
#
# runner = AutoTest(suite=suite, name='用例调试', to_user=to_user, case_type='M', env=env)
# runner.run()
