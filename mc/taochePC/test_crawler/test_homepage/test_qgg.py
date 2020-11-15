# coding = utf-8
# 开发团队 ：
# 开发人员 ：lennonhui
# 开发时间 ：2020/7/29 10:06 PM
# 文件名称 ：test_qgg.py
# 开发工具 ：PyCharm


from titan import tt_check
from taochePC.base import Base
from taochePC import locator
from taochePC.config import config

url = config.home_url

class qgg_floor(Base):

    def test_qgg(self):
        """测试首页全国购楼层跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.qgg).click()
        self.driver.pause(3)
        self.driver.switch_to_window()
        tag_is_dispayed = self.driver.is_display(locator.HeaderLocator.qgg_tag)
        self.driver.pause(3)
        tt_check.assertTrue(tag_is_dispayed, "列表页全国购签是否显示：%s" % tag_is_dispayed)

    def test_qgg(self):
        """测试首页全国购楼层-查看全部跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.qgg_see).click()
        self.driver.pause(3)
        self.driver.switch_to_window()
        tag_is_dispayed = self.driver.is_display(locator.HeaderLocator.qgg_tag)
        self.driver.pause(3)
        tt_check.assertTrue(tag_is_dispayed, "列表页全国购签是否显示：%s" % tag_is_dispayed)

    def test_qgg_img(self):
        """测试首页全国购楼层-车图-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.Qgg_img).click()
        self.driver.pause(3)
        self.driver.switch_to_window()
        img_is_dispayed = self.driver.is_display(locator.HeaderLocator.car_img)
        self.driver.pause(3)
        tt_check.assertTrue(img_is_dispayed, "详情页大图是否显示：%s" % img_is_dispayed)

    def test_qgg_car(self):
        """测试首页全国购楼层-车名称-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.car_name).click()
        self.driver.pause(3)
        self.driver.switch_to_window()
        img_is_dispayed = self.driver.is_display(locator.HeaderLocator.car_img)
        self.driver.pause(3)
        tt_check.assertTrue(img_is_dispayed, "详情页大图是否显示：%s" % img_is_dispayed)







