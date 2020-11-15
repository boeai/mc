# coding = utf-8
# 开发团队 ：
# 开发人员 ：lennonhui
# 开发时间 ：2020/7/29 10:53 PM
# 文件名称 ：test_about.py
# 开发工具 ：PyCharm



from titan import tt_check
from taochePC.base import Base
from taochePC import locator
from taochePC.config import config
import requests
url = config.home_url

class about(Base):

    def test_about(self):
        """测试首页底部关于淘车-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.about_button).click()
        self.driver.pause(3)
        self.driver.switch_to_window()
        about_is_dispayed = self.driver.is_display(locator.HeaderLocator.about_title)
        self.driver.pause(3)
        tt_check.assertTrue(about_is_dispayed, "关于我们标题是否显示：%s" % about_is_dispayed)

    def test_contact(self):
        """测试首页底部联系我们-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.contact_button).click()
        self.driver.pause(3)
        self.driver.switch_to_window()
        about_is_dispayed = self.driver.is_display(locator.HeaderLocator.about_title)
        self.driver.pause(3)
        tt_check.assertTrue(about_is_dispayed, "关于我们标题是否显示：%s" % about_is_dispayed)
    #
    def test_B_lisence(self):
        """测试首页底部营业执照-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        B_li = self.driver.find_element(locator.HeaderLocator.license_url).get_attribute('href')
        # 获取营业执照的请求状态
        r = requests.get(B_li)
        status = r.status_code
        print(status)
        tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)

    def test_B_ICP(self):
        """测试首页底部ICP证-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        ICP_li = self.driver.find_element(locator.HeaderLocator.ICP_url).get_attribute('href')
        # 获取ICP证的请求状态
        r = requests.get(ICP_li)
        status = r.status_code
        tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)

    def test_B_TV(self):
        """测试首页底部广播电视许可证-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        TV_li = self.driver.find_element(locator.HeaderLocator.TV_url).get_attribute('href')
        # 获取广播电视许可证的请求状态
        r = requests.get(TV_li)
        status = r.status_code
        tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)