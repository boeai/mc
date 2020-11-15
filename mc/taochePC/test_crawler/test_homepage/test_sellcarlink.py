# coding = utf-8
# 开发团队 ：
# 开发人员 ：lennonhui
# 开发时间 ：2020/7/29 9:08 PM
# 文件名称 ：test_sellcarlink.py
# 开发工具 ：PyCharm


from titan import tt_check
from taochePC.base import Base
from taochePC import locator
from taochePC.config import config

url = config.home_url

class sellcar(Base):

    def test_Isellcar1(self):
        """测试首页我要卖车跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.Isellcar).click()
        #self.driver.pause(3)
        sell_is_dispayed = self.driver.is_display(locator.HeaderLocator.sell_img)
        #self.driver.pause(3)
        tt_check.assertTrue(sell_is_dispayed, "我要卖车页是否显示：%s" % sell_is_dispayed)

    def test_Isellcar2(self):
        """测试首页我要卖车按钮跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.Isellcarbutton).click()
        #self.driver.pause(3)
        sell_is_dispayed = self.driver.is_display(locator.HeaderLocator.sell_img)
        #self.driver.pause(3)
        tt_check.assertTrue(sell_is_dispayed, "我要卖车页是否显示：%s" % sell_is_dispayed)

    def test_Isellcar3(self):
        """测试首页免费估价按钮跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.pinggu_button).click()
        #self.driver.pause(3)
        pinggu_is_dispayed = self.driver.is_display(locator.HeaderLocator.pinggu_img)
        #self.driver.pause(3)
        tt_check.assertTrue(pinggu_is_dispayed, "免费估价页是否显示：%s" % pinggu_is_dispayed)


