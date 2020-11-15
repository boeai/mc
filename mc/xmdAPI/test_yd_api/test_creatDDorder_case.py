# 创建订单

from xmdAPI.base import Base
from xmdAPI.test_yd_api.process_fuc import helpXJTG
from xmdAPI.test_yd_api.common_fuc import helpCreateYUNOrder
from xmdAPI.test_yd_api.common_fuc import getGDInfo




class TestCREATDDORDERCase(Base):
    '''
    {
    	"orderNo": "GD157456593136874",
    	"deposit": "1050",
    	"customerName": "18101554258",
    	"remark": "我是备注哈哈哈",
    	"customerType": "1",
    	"buyerNumber": "110222110222",
    	"customerPhone": "18101554258"
    }

    '''
    def test_CreatOrderSuccess(self):
        """测试添加创建订单接口,创建订单成功，@author:liusai"""
        ord = helpXJTG(self)
        ordInfo = getGDInfo(ord)
        customerPhone = ordInfo['data']['customerMobile']
        result = helpCreateYUNOrder(ord,
                                    "1000",
                                    customerPhone,
                                    "我是备注",
                                    "1",
                                    "1102002002002",
                                    customerPhone)
        self.assertEqual(result['code'],200)

    def test_CreatOrderFail_ordNoEmpty(self):
        """测试添加创建订单接口,创建订单失败，工单号为空，@author:liusai"""
        ord = helpXJTG(self)
        ordInfo = getGDInfo(ord)
        customerPhone = ordInfo['data']['customerMobile']
        result = helpCreateYUNOrder("",
                                    "1000",
                                    customerPhone,
                                    "我是备注",
                                    "1",
                                    "1102002002002",
                                    customerPhone)
        self.assertIn('没有查到当前工单',result['message'])

    def test_CreatOrderFail_ordNoNOlife(self):
        """测试添加创建订单接口,创建订单失败，工单号不存在，@author:liusai"""
        ord = helpXJTG(self)
        ordInfo = getGDInfo(ord)
        customerPhone = ordInfo['data']['customerMobile']
        result = helpCreateYUNOrder("ddddddddd",
                                    "1000",
                                    customerPhone,
                                    "我是备注",
                                    "1",
                                    "1102002002002",
                                    customerPhone)

        self.assertIn('没有查到当前工单', result['message'])


    def test_CreatOrderFail_depositEmpty(self):
        """测试添加创建订单接口,创建订单失败，定金金额为空，@author:liusai"""
        ord = helpXJTG(self)
        ordInfo = getGDInfo(ord)
        customerPhone = ordInfo['data']['customerMobile']
        result = helpCreateYUNOrder(ord,
                                    "",
                                    customerPhone,
                                    "我是备注",
                                    "1",
                                    "1102002002002",
                                    customerPhone)
        self.assertIn('定金不能为空', result['message'])

    def test_CreatOrderFail_buyerNumberEmpty(self):
        """测试添加创建订单接口,创建订单失败，buyerNumber为空，@author:liusai"""
        ord = helpXJTG(self)
        ordInfo = getGDInfo(ord)
        customerPhone = ordInfo['data']['customerMobile']
        result = helpCreateYUNOrder(ord,
                                    "10000",
                                    customerPhone,
                                    "我是备注",
                                    "1",
                                    "",
                                    customerPhone)
        self.assertIn('客户身份证号不能为空', result['message'])

    def test_CreatOrderFail_customerPhoneEmpty(self):
        """测试添加创建订单接口,创建订单失败，buyerNumber为空，@author:liusai"""
        ord = helpXJTG(self)
        ordInfo = getGDInfo(ord)
        customerPhone = ordInfo['data']['customerMobile']
        result = helpCreateYUNOrder(ord,
                                    "10000",
                                    customerPhone,
                                    "我是备注",
                                    "1",
                                    "1102002002002",
                                    '')
        self.assertEqual(result['code'], 200)


    def test_CreatOrderSuccess_customerTypeEmpty(self):
        """测试添加创建订单接口,创建订单成功，customerType为空，@author:liusai"""
        ord = helpXJTG(self)
        ordInfo = getGDInfo(ord)
        customerPhone = ordInfo['data']['customerMobile']
        result = helpCreateYUNOrder(ord,
                                    "1000",
                                    customerPhone,
                                    "我是备注",
                                    "",
                                    "1102002002002",
                                    customerPhone)
        self.assertEqual(result['code'], 200)



    def test_CreatOrderSuccess_customerNameEmpty(self):
        """测试添加创建订单接口,创建订单成功，customerName为空，@author:liusai"""
        ord = helpXJTG(self)
        ordInfo = getGDInfo(ord)
        customerPhone = ordInfo['data']['customerMobile']
        result = helpCreateYUNOrder(ord,
                                    "1000",
                                    "",
                                    "我是备注",
                                    "1",
                                    "1102002002002",
                                    customerPhone)
        self.assertEqual(result['code'],200)

    def test_CreatOrderSuccess_remarkEmpty(self):
        """测试添加创建订单接口,创建订单成功，remark为空，@author:liusai"""
        ord = helpXJTG(self)
        ordInfo = getGDInfo(ord)
        customerPhone = ordInfo['data']['customerMobile']
        result = helpCreateYUNOrder(ord,
                                    "1000",
                                    customerPhone,
                                    "",
                                    "1",
                                    "1102002002002",
                                    customerPhone)
        self.assertEqual(result['code'],200)

