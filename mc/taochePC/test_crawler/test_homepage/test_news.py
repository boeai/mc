# coding = utf-8
# 开发团队 ：
# 开发人员 ：lennonhui
# 开发时间 ：2020/7/29 10:52 PM
# 文件名称 ：test_news.py
# 开发工具 ：PyCharm



from titan import tt_check
from taochePC.base import Base
from taochePC import locator
from taochePC.config import config

url = config.home_url

class news(Base):

    def test_news_all(self):
        """测试首页资讯楼层-查看全部跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.news_see).click()
        self.driver.pause(3)
        self.driver.switch_to_window()
        news_is_dispayed = self.driver.is_display(locator.HeaderLocator.news_title)
        self.driver.pause(3)
        tt_check.assertTrue(news_is_dispayed, "淘车试驾标题是否显示：%s" % news_is_dispayed)

    # def test_news_img(self):
    #     """测试首页资讯楼层-大图跳转,@author:xulanzhong"""
    #     self.driver.get(url)
    #     self.driver.max_window()
    #     self.driver.find_element(locator.HeaderLocator.fist_img).click()
    #     self.driver.pause(3)
    #     self.driver.switch_to_window()
    #     brand_is_dispayed = self.driver.is_display(locator.HeaderLocator.new_brand)
    #     self.driver.pause(3)
    #     tt_check.assertTrue(brand_is_dispayed, "新车页品牌是否显示：%s" % brand_is_dispayed)
    #
    #
    # def test_calculater(self):
    #     """测试首页新车楼层-购车计算器跳转,@author:xulanzhong"""
    #     self.driver.get(url)
    #     self.driver.max_window()
    #     self.driver.find_element(locator.HeaderLocator.calculater).click()
    #     self.driver.pause(3)
    #     self.driver.switch_to_window()
    #     # tag_is_dispayed = self.driver.is_display(locator.HeaderLocator.qgg_tag)
    #     # self.driver.pause(3)
    #     # tt_check.assertTrue(tag_is_dispayed, "列表页全国购签是否显示：%s" % tag_is_dispayed)
    #
    #     actual_calculater_img = self.driver.find_element(locator.HeaderLocator.calculater_button).text
    #     expect_calculater_img = '分期购车计算器'
    #     tt_check.assertEqual(expect_calculater_img, actual_calculater_img,
    #                          "分期计算器页面，期望是%s，实际是%s" % (expect_calculater_img, actual_calculater_img))
    #
    # def test_fenqi(self):
    #     """测试首页新车楼层-分期购车-跳转,@author:xulanzhong"""
    #     self.driver.get(url)
    #     self.driver.max_window()
    #     self.driver.find_element(locator.HeaderLocator.fenqi_buy).click()
    #     self.driver.pause(3)
    #     self.driver.switch_to_window()
    #     fenqi_is_dispayed = self.driver.is_display(locator.HeaderLocator.fenqi_img)
    #     self.driver.pause(3)
    #     tt_check.assertTrue(fenqi_is_dispayed, "分期购车页新车专享是否显示：%s" % fenqi_is_dispayed)
    #
    # def test_online_buy(self):
    #     """测试首页新车楼层-在线购车-跳转,@author:xulanzhong"""
    #     self.driver.get(url)
    #     self.driver.max_window()
    #     self.driver.find_element(locator.HeaderLocator.online_buy).click()
    #     self.driver.pause(3)
    #     self.driver.switch_to_window()
    #     online_is_dispayed = self.driver.is_display(locator.HeaderLocator.online_name)
    #     self.driver.pause(3)
    #     tt_check.assertTrue(online_is_dispayed, "在线购车页帮您分期是否显示：%s" % online_is_dispayed)
    #
    # def test_TC_tiyandian(self):
    #     """测试首页新车楼层-淘车体验店-跳转,@author:xulanzhong"""
    #     self.driver.get(url)
    #     self.driver.max_window()
    #     self.driver.find_element(locator.HeaderLocator.tiyandian).click()
    #     self.driver.pause(3)
    #     self.driver.switch_to_window()
    #     tiyandian_is_dispayed = self.driver.is_display(locator.HeaderLocator.tiyandian_name)
    #     self.driver.pause(3)
    #     tt_check.assertTrue(tiyandian_is_dispayed, "淘车体验店页重庆体验店是否显示：%s" % tiyandian_is_dispayed)