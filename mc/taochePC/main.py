# -*- coding:utf-8 -*-
import unittest
from service import AutoTest
from taochePC.config import config

# 企业微信通知名单
to_user = config.to_user
# 环境标识
env = config.env


# 当前目录
test_dir = "./test_crawler/"
# 自动加载test_dir下所有以test开头的文件中以test开头的测试方法
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
runner = AutoTest(suite=discover, name='用例调试', to_user=to_user, case_type='PC', env=env)
runner.run()



# # 生成报告
# runner = ResultHandle(suite=discover, name='淘车PC测试', to_user=to_user, case_type='PC', env=env)
# runner.run()


# 调试单个用例
# from taochePC.test_buycar.test_detail import Detail
# suite = unittest.TestSuite()
# suite.addTest(Detail('test_addCollect'))
# #
# runner = AutoTest(suite=suite, name='用例调试', to_user=to_user, case_type='PC', env=env)
# runner.run()
