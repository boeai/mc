from taocheApp import Base, HomeLoctor
from titan import tt_check

class TuiJian(Base):
    def test_tuijian_floor(self):
        """首页推荐区点击检查@author:anyingying"""
        self.driver.sleep(4)
        print("寻找推荐楼层")
        self.driver.swipeUpDown(0.3, 0.1)
        print("定位到推荐楼层")

        mainTitleList = self.driver.find_elements(HomeLoctor.JINRISHANGXIN_TEXT_IDS)
        if mainTitleList:
            mainTitletext = mainTitleList[0].text
            print(mainTitletext)
            tt_check.assertEqual("今日上新",mainTitletext,"推荐区域主标题，期望是今日上新，实际是%s" % mainTitletext)
            # 测试今日上新&越野SUV
            reclist = self.driver.find_elements(HomeLoctor.JINRISHANGXIN_IDS)
            for rec in reclist:
                rec.click()
                self.driver.sleep(2)
                shaixuanText = self.driver.find_element(HomeLoctor.CAR_LIST_SCREEN_ID).find_element_by_class_name('android.widget.TextView').text
                print("列表页回显关键词为%s" % shaixuanText)
                tt_check.assertIn(shaixuanText ,"今日上新或者SUV", "期望是今日上新或者SUV，实际是%s" % shaixuanText)
                self.driver.find_element(HomeLoctor.SHOUYE_ID).click()
                self.driver.sleep(1)

            #测试准新车&超低月供&高端品质
            recslist = self.driver.find_elements(HomeLoctor.ZHUNXINCHE_IDS)
            for recs in recslist:
                recs.click()
                self.driver.sleep(2)
                shaixuanText = self.driver.find_element(HomeLoctor.CAR_LIST_SCREEN_ID).find_element_by_class_name(
                    'android.widget.TextView').text
                print("列表页回显关键词为%s" % shaixuanText)
                tt_check.assertIn(shaixuanText ,"准新车或2000元以下或20-40万", "期望是准新车或2000元以下或20-40万，实际是%s" % shaixuanText)
                self.driver.find_element(HomeLoctor.SHOUYE_ID).click()
                self.driver.sleep(1)

        else:
            print("首页没有取到推荐楼层")
