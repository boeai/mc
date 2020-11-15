# coding = utf-8
# 开发团队 ：
# 开发人员 ：lennonhui
# 开发时间 ：2020/7/28 1:55 PM
# 文件名称 ：test_logo.py
# 开发工具 ：PyCharm

from titan import tt_check
from taochePC.base import Base
from taochePC import locator
from taochePC.config import config

url = config.home_url

class Logo(Base):

    def test_logo(self):
        """测试首页logo是否展示,@author:xulanzhong"""
        self.driver.get(url)
        logo_is_dispayed = self.driver.is_display(locator.HeaderLocator.LOGO)
        self.driver.pause(3)
        tt_check.assertTrue(logo_is_dispayed, "首页Logo是否显示：%s" % logo_is_dispayed)