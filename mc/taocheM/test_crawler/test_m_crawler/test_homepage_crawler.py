# coding = utf-8
# 开发团队 ：
# 开发人员 ：lennonhui
# 开发时间 ：2020/8/10 10:14 PM
# 文件名称 ：test_homepage_crawler.py
# 开发工具 ：PyCharm

from titan import tt_check
from taocheM.base_m import Base
from taocheM import locator_m
from taocheM.config_m import config
import requests


home_url = config.home_url

class M_home_crawler(Base):

    def test_M_homepage(self):
        """遍历M首页链接并验证状态码,@author:xulanzhong"""
        self.driver.get(home_url)
        #self.driver.max_window()
        # 匹配出所有a元素里的链接
        urls = self.driver.find_elements(locator_m.Locator_Home.xpath_all)
        print("当前页面的可用链接如下：")

        for url in urls:
           u = url.get_attribute('href')
           if u == 'None':  # 排除没有链接的元素
               continue
           try:
               r = requests.get(u)
               status = r.status_code
               tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)
           except:
               # 把测试不通过的url显示出来
               print('Error url  : ' + str(u) + ':++++++++不是正确链接+++++++')  # 把测试不通过的url显示出来
           else:
               # 测试通过的url展示出来
               print(u)
