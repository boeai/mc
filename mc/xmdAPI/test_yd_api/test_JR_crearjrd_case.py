#创建金融单
from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpCreatFinanceOrder
from xmdAPI.test_yd_api.process_fuc import getOrderNumber
from xmdAPI.test_yd_api.process_fuc import helpXJTG

class TestJRCREATJRDCase(Base):

    #创建金融单成功
    def test_creatFinanceSuccess(self):
        """测试创建金融单接口,创建成功，@author:liusai"""
        orderNo = getOrderNumber(self)
        result = helpCreatFinanceOrder(orderNo)

        self.assertEqual(result['code'],200)

    #创建金融单失败
    def test_creatFinanceFail_orderNoEmpty(self):
        """测试创建金融单接口,创建失败，orderNo为空，@author:liusai"""
        result = helpCreatFinanceOrder('')
        self.assertIn('工单不存在',result['message'])

    #创建金融单失败
    def test_creatFinanceSuccess_orderNoOver(self):
        """测试创建金融单接口,创建失败，orderNo已经创建过，@author:liusai"""
        ord = helpXJTG(self)
        result = helpCreatFinanceOrder(ord)
        self.assertEqual(result['code'],200)
