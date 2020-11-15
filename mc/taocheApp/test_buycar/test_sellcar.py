import time

from taocheApp import Base, BuyCarLocator,SellCarLocator
from titan import tt_check




class SellCar(Base):
    def test_sellcar(self):
        """app卖车tab跳转@author:kangjuan"""
        self.driver.find_element(SellCarLocator.TAB).click()
        titleText=self.driver.find_element(SellCarLocator.TITLE).text
        if titleText=="卖车":
            print("卖车页正确")

        else:
            print("卖车页错误")







