# -*- coding:utf-8 -*-
import unittest
from service import AutoTest
from taochePC.config import config

# 企业微信通知名单
to_user = config.to_user
# 环境标识
env = config.env
# 当前目录
test_dir = "./"

# # 自动加载test_dir下所有以test开头的文件中以test开头的测试方法
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
#
#
# # 生成报告
# runner = AutoTest(suite=discover, name='淘车API测试', to_user=to_user, case_type='API', env=env)
# runner.run()


# 调试单个用例
from taocheAPI.test_pc_api.test_pc_homepage import HomePageAPI
suite = unittest.TestSuite()
suite.addTest(HomePageAPI('test_getbaozhencar'))

runner = AutoTest(suite=suite, name='API用例调试', to_user=to_user, case_type='API', env=env)
runner.run()
