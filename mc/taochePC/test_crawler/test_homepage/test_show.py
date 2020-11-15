# coding = utf-8
# 开发团队 ：
# 开发人员 ：lennonhui
# 开发时间 ：2020/7/29 10:52 PM
# 文件名称 ：test_show.py
# 开发工具 ：PyCharm



from titan import tt_check
from taochePC.base import Base
from taochePC import locator
from taochePC.config import config

url = config.home_url

class buyershow(Base):

    def test_seeall(self):
        """测试首页买家秀楼层-查看全部跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.see_button).click()
        self.driver.pause(3)
        self.driver.switch_to_window()
        show_is_dispayed = self.driver.is_display(locator.HeaderLocator.show_title)
        self.driver.pause(3)
        tt_check.assertTrue(show_is_dispayed, "买家秀列表标题是否显示：%s" % show_is_dispayed)

    def test_show_img(self):
        """测试首页买家秀楼层-首图跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.show_button).click()
        self.driver.pause(3)
        self.driver.switch_to_window()
        show_is_dispayed = self.driver.is_display(locator.HeaderLocator.show_title)
        self.driver.pause(3)
        tt_check.assertTrue(show_is_dispayed, "买家秀列表标题是否显示：%s" % show_is_dispayed)
