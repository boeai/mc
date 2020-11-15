# coding = utf-8
# 开发团队 ：
# 开发人员 ：lennonhui
# 开发时间 ：2020/7/31 8:52 AM
# 文件名称 ：test_detail_crawler.py
# 开发工具 ：PyCharm



from titan import tt_check
from taochePC.base import Base
from taochePC import locator
from taochePC.config import config
import requests


buycar_url = config.bj_buycar_url

class PC_detail_crawler(Base):

    def test_pc_detail(self):
        """测试列表页爬取链接并验证状态码,@author:xulanzhong"""
        self.driver.get(buycar_url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.first_car).click()
        self.driver.switch_to_window()
        pagesource = self.driver.get_url()
        print('当前页面的url是:',pagesource)
        urls = self.driver.find_elements(locator.HeaderLocator.xpath_all)  # 匹配出所有a元素里的链接
        print("当前页面的可用链接如下：")

        for url in urls:
            u = url.get_attribute('href')
            if u == 'None':  # 很多的a元素没有链接，所有是None
               continue
            try:
                r = requests.get(u)
                status = r.status_code
                tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)
            except:
                print('Error url  : ' + str(u) + ':++++++++不是正确链接+++++++')  # 把测试不通过的url显示出来
            else:
                print(u)  # 测试通过的url展示出来
