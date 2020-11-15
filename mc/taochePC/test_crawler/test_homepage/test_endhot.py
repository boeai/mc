# coding = utf-8
# 开发团队 ：
# 开发人员 ：lennonhui
# 开发时间 ：2020/7/29 10:54 PM
# 文件名称 ：test_endhot.py
# 开发工具 ：PyCharm


from titan import tt_check
from taochePC.base import Base
from taochePC import locator
from taochePC.config import config
import requests
url = config.home_url

class hot_other(Base):

    def test_hot_city(self):
        """测试首页底部热门城市-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        shanghai_li = self.driver.find_element(locator.HeaderLocator.hot_shanghai).get_attribute('href')
        r = requests.get(shanghai_li)
        status = r.status_code
        tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)

    def test_hot_brand(self):
        """测试首页底部热门品牌-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        brand_li = self.driver.find_element(locator.HeaderLocator.hot_brand).get_attribute('href')
        r = requests.get(brand_li)
        status = r.status_code
        tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)

    def test_hot_series(self):
        """测试首页底部热门车系-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        series_li = self.driver.find_element(locator.HeaderLocator.hot_series).get_attribute('href')
        r = requests.get(series_li)
        status = r.status_code
        tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)

    def test_hot_car(self):
        """测试首页底部车型库-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        car_li = self.driver.find_element(locator.HeaderLocator.hot_car).get_attribute('href')
        r = requests.get(car_li)
        status = r.status_code
        tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)

    def test_TC_ask(self):
        """测试首页底部淘车问答-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        ask_li = self.driver.find_element(locator.HeaderLocator.car_ask).get_attribute('href')
        r = requests.get(ask_li)
        status = r.status_code
        tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)

    def test_TC_news(self):
        """测试首页底部淘车资讯-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        news_li = self.driver.find_element(locator.HeaderLocator.car_news).get_attribute('href')
        r = requests.get(news_li)
        status = r.status_code
        tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)

    def test_car_vehicle(self):
        """测试首页底部淘车车型-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        vehicle_li = self.driver.find_element(locator.HeaderLocator.car_vehicle).get_attribute('href')
        r = requests.get(vehicle_li)
        status = r.status_code
        tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)

    def test_car_find(self):
        """测试首页底部找二手车-跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        car_li = self.driver.find_element(locator.HeaderLocator.find_car).get_attribute('href')
        r = requests.get(car_li)
        status = r.status_code
        tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)