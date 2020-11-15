#申请线下收款

from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpOfflineTransfer
from xmdAPI.test_yd_api.common_fuc import getDDList

class TestOFFLINETRANSFERCase(Base):
    '''
    {
    "orderId": "${orderId}",订单号
    "payType": 1,1 定金 2 尾款 3 其他
    "transactionSum": "${deposit}",支付金额
    "transactionForm": 2,收款类型 1 信用卡 2 现金 3 其他
    "useCreditCardPay": 0, 是否使用信用卡 使用true，不使用false
    "isExclusiveAccount": 1, 1 是 0 不是
    "transactionType": 6 收款方式 5:线上 6:线下
    }
    '''
    def test_applySuccess(self):
        ddList = getDDList()
        ordInfo=ddList['data']['topicList'][0]['orderId']
        result = helpOfflineTransfer(ordInfo,
                                     '1',
                                     '1000',
                                     '2',
                                     0,
                                     '1',
                                     '6')
        print(result)
        self.assertEqual('SUCCESS',result['message'])

