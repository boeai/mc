# coding = utf-8
# 开发团队 ：
# 开发人员 ：lennonhui
# 开发时间 ：2020/7/28 8:37 PM
# 文件名称 ：test_AD.py
# 开发工具 ：PyCharm

from titan import tt_check
from taochePC.base import Base
from taochePC import locator
from taochePC.config import config

url = config.home_url

class AD(Base):

    def test_AD(self):
        """测试首页北京焦点图保真说明跳转,@author:xulanzhong"""
        self.driver.get(url)
        self.driver.max_window()
        self.driver.find_element(locator.HeaderLocator.BJAD).click()
        self.driver.pause(3)
        AD_is_dispayed = self.driver.is_display(locator.HeaderLocator.BZAD)
        tt_check.assertTrue(AD_is_dispayed, "保真说明页是否显示：%s" % AD_is_dispayed)