# coding = utf-8
# 开发团队 ：
# 开发人员 ：lennonhui
# 开发时间 ：2020/7/28 8:55 PM
# 文件名称 ：test_buycarlink.py
# 开发工具 ：PyCharm


from titan import tt_check
from taochePC.base import Base
from taochePC import locator
from taochePC.config import config

url = config.home_url

class buycar(Base):

    def test_Ibuycar(self):
        """测试首页我要买车跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.Ibuycar).click()
        self.driver.pause(3)
        actual_bjbc = self.driver.find_element(locator.HeaderLocator.BJbuycar).text
        expect_bjbc = '北京二手车'
        tt_check.assertEqual(expect_bjbc, actual_bjbc,"二手车列表面包屑，期望是%s，实际是%s" % (expect_bjbc, actual_bjbc))

    def test_car_price(self):
        """测试首页我要买车-价格跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.Car_price).click()
        self.driver.pause(3)
        self.driver.switch_to_window()
        actual_price_path = self.driver.find_element(locator.HeaderLocator.Price_path).title
        expect_price_path = '8-10万'
        tt_check.assertEqual(expect_price_path, actual_price_path,"二手车列表面包屑，期望是%s，实际是%s" % (expect_price_path, actual_price_path))

    def test_brand_name(self):
        """测试首页我要买车-品牌跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.brand_name).click()
        self.driver.switch_to_window()
        tag_is_dispayed = self.driver.is_display(locator.HeaderLocator.bz_tag)
        self.driver.pause(3)
        tt_check.assertTrue(tag_is_dispayed, "列表页直营签是否显示：%s" % tag_is_dispayed)

    def test_car_level(self):
        """测试首页我要买车-级别跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.Car_level).click()
        self.driver.pause(3)
        self.driver.switch_to_window()
        actual_level_path = self.driver.find_element(locator.HeaderLocator.Level_path).text
        expect_level_path = '小型车'
        tt_check.assertEqual(expect_level_path, actual_level_path,
                             "二手车列表面包屑，期望是%s，实际是%s" % (expect_level_path, actual_level_path))