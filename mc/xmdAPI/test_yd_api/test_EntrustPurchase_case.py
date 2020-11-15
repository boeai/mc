#采购协议电子签

from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import getDDList
from xmdAPI.test_yd_api.common_fuc import helpEntruePurchase


class TestENTUREPURCHASECase(Base):
    '''
    {
    "orderId":"201903060001",
    "partyAName":"小王",
    "partyAIdCard":"123456789098765",
    "partyAContactsName":"小王",
    "partyAPhone":"15910521111",
    "partyAAddress":"小王村",
    "carName":"大众甲壳虫2018款3.0T自动舒适版",
    "vinCode":"ENM2991LHK",
    "buyCarType":1,购车方式（1全款 2 金融 ）
    "dealPrice":"3000000",
    "advanceChargePrice":"2989988999",车辆预付价款
    "storageChargePrice":"500",仓储费标准
    "firstPaymentPrice":"30000"车辆首付款
    }
    '''

    def test_Purchase_Success(self):
        """测试采购协议电子签,发起电子签成功，@author:liusai"""
        ddList = getDDList()
        ordInfo = ddList['data']['topicList'][0]['orderId']

        result = helpEntruePurchase(ordInfo,
                                    '刘赛',
                                    '110222198912223524',
                                    '刘赛',
                                    '18510169951',
                                    '客户地址',
                                    '车型',
                                    'vincode',
                                    1,
                                    500000,
                                    '30000',
                                    '1500',
                                    '10000')
        print(result)
        self.assertEqual('SUCCESS',result['message'])


