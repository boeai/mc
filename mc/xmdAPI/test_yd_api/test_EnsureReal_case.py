# 订单电子签（保真协议）
from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpEnsureReal
from xmdAPI.test_yd_api.common_fuc import getDDList

class TestEnsureRealCase(Base):

    '''
    {
	"carMileage": "111100",
	"orderId": "20191124752483",
	"partyAPhone": "18101554260",
	"carName": "Audi Sport 2017款 2.5T Limousine",
	"agreementTakeEffectDate": "2019-11-27",
	"partyAName": "18101554260",
	"vinCode": "EZKVHFRP5C26D5YM0",
	"partyAIdCard": "22072418880201262565",
	"dealPrice": "500000",
	"type": "21"
    }
    '''
    def test_EnsureReal_Success(self):
        """测试保真协议电子签,发起电子签成功，@author:liusai"""
        ddList = getDDList()
        ordInfo = ddList['data']['topicList'][0]['orderId']

        result = helpEnsureReal('2100',
                                ordInfo,
                                '18510169951',
                                "Audi Sport 2017款 2.5T Limousine",
                                '2019-08-01',
                                "刘赛",
                                '6U91VK5J8HT8BAE2C',
                                '110222198912223524',
                                '500000',
                                '21')

        print(result)
        self.assertEqual('SUCCESS',result['message'])