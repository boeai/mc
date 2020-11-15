import time

from taocheApp import Base, BuyCarLocator,SellCarLocator
from titan import tt_check



class BuyCar(Base):
    def test_buycarjiage(self):
        """app买车tab跳转,打开城市选择，选择沈阳，关闭城市选择@author:kangjuan"""
        self.driver.find_element(BuyCarLocator.TAB).click()#点击买车TAB
       #self.driver.find_element(BuyCarLocator.CITY).click()#打开城市选择框
       #self.driver.find_element(BuyCarLocator.SY).click()#选择沈阳
       # self.driver.find_element(BuyCarLocator.CITY_CLOSE).click()#关闭城市选择框
        self.driver.find_element(BuyCarLocator.JG).click()#点击价格筛选框
        self.driver.find_element(BuyCarLocator.JG1).click()#选择价格100万以上
        self.driver.find_element(BuyCarLocator.PX).click()#点击排序筛选框
        self.driver.find_element(BuyCarLocator.JGZD).click()#选择价格最低
        Text=self.driver.find_element(BuyCarLocator.JGFIRST).text #第一辆车的价格
        print("筛选的100万以上的车源中价格最低的车源价格是",Text)


        # def test_buycarsearch(self):
        #     """app买车tab跳转,打开城市选择，选择沈阳，关闭城市选择@author:kangjuan"""
        #     self.driver.find_element(BuyCarLocator.TAB).click()  # 点击买车TAB
        #     self.driver.find_element(BuyCarLocator.SEARCH_INPUT).click().sendkeys("奥迪")  # 搜索框输入奥迪












