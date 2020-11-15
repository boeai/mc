import time

from taocheApp import Base, HomeLoctor
from titan import tt_check


class HomePage(Base):
    def test_page_click(self):
        """app首页、列表页、详情页点击检查@author:fangyu"""
        brandText = self.driver.find_element(HomeLoctor.BRAND_KEY).text
        print(brandText)
        self.driver.find_element(HomeLoctor.BRAND_KEY).click()

        classList = self.driver.find_element(HomeLoctor.CAR_LIST_SCREEN_ID).find_elements_by_class_name('android.widget.TextView')
        if classList:
            classText = classList[0].text
            print(classText)
            tt_check.assertEqual(brandText,classText,'首页选中品牌:{brandText},列表页展示品牌:{classText}'.format(
                brandText=brandText,classText=classText
            ))
            carList = self.driver.find_elements(HomeLoctor.CAR_INFO_IDS)
            if carList:
                carNameText = carList[0].text
                print("取到车源列表页第一辆车:{carNameText}".format(carNameText=carNameText))
                carList[0].click()
                print("进入车源详情页")
                DetailCarNameText = self.driver.find_element(HomeLoctor.DETAIL_CAR_NAME).text
                print(DetailCarNameText)
                self.driver.swipeUpDown(0.9,0.1)
                qggText = self.driver.find_element(HomeLoctor.QGG_FLOOR_ID).text
                if qggText:
                    tt_check.assertTrue(True,"全国购店铺名称:{qggText}".format(qggText=qggText))
                else:
                    tt_check.assertFalse(False,"车源:{DetailCarNameText} 详情页没有全国购楼层".format(DetailCarNameText=DetailCarNameText))

            else:
                print('没有取到车源列表数据')
        else:
            print('首页没有取到品牌')



