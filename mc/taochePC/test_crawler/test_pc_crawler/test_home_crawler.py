# coding = utf-8
# 开发团队 ：
# 开发人员 ：lennonhui
# 开发时间 ：2020/7/30 12:06 PM
# 文件名称 ：test_home_crawler.py
# 开发工具 ：PyCharm


from titan import tt_check
from taochePC.base import Base
from taochePC import locator
from taochePC.config import config
import requests


home_url = config.home_url

class PC_home_crawler(Base):

    def test_pc_homepage(self):
        """测试首页爬取链接并验证状态码,@author:xulanzhong"""
        self.driver.get(home_url)
        self.driver.max_window()
        # 匹配出所有a元素里的链接
        urls = self.driver.find_elements(locator.HeaderLocator.xpath_all)
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
               print('Error url:   ' + u)
           else:
               # 测试通过的url展示出来
               print(u)
