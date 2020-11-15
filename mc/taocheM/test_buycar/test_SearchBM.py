# -*- coding:utf-8 -*-
#@author:xulanzhong
from titan import tt_check
from taocheM.base_m import Base
from taocheM import locator_m
from taocheM.config_m import config

url = config.list_url



class searchbm(Base):

    def test_bm(self):
        """测试列表页搜索奔驰结果是否展示,@author:xulanzhong"""

        self.driver.get(url)

        self.driver.click(locator_m.Locator_BuyCar.bz_click)

        bz_is_dispayed = self.driver.is_display(locator_m.Locator_BuyCar.bz_list)

        tt_check.assertTrue(bz_is_dispayed, "宝马车源名称是否显示：%s" % bz_is_dispayed)

