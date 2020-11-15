# 订单电子签（车辆交接函）
from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpHandoverConfirm

from xmdAPI.test_yd_api.common_fuc import getDDList

class TestHandoverConfirmCase(Base):


    '''
    {
	"partyBIdCard": "2939393993",
	"carName": "Audi Sport 2017款 2.5T Limousine",
	"partyAName": "18101554260",
	"carTransferDate": "2019-12-24",
	"vinCode": "EZKVHFRP5C26D5YM0",
	"partyAPhone": "18101554260",
	"partyBPhone": "18164664999",
	"signDate": "2019-11-26",
	"orderId": "20191124752483",
	"remark": "嗯嗯对",
	"partyAIdCard": "22072418880201262565",
	"entrustPurchaseContractId": "QY2019112400824",
	"subsidiaryData": "内心的那女的",
	"partyBName": "看看"
    }

    '''
    def test_handoverconfirm_Success(self):
        """测试采购协议电子签,发起电子签成功，@author:liusai"""
        ddList = getDDList()
        ordInfo = ddList['data']['topicList'][0]['orderId']

        result = helpHandoverConfirm("2939393993",
                                     "Audi Sport 2017款 2.5T Limousine",
                                     "刘赛",
                                     "2019-12-24",
                                     "EZKVHFRP5C26D5YM0",
                                     "18510169951",
                                     "18164664999",
                                     '2019-11-26',
                                     ordInfo,
                                     "我是备注哈哈哈",
                                     "110222198912223524",
                                     "QY2019112400824",
                                     "内心的那女的",
                                     "看看")

        print(result)