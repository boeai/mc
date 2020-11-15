#重新分配case
# -*- coding=UTF-8 -*-

from xmdAPI.base import Base

from xmdAPI.test_yd_api.common_fuc import helpReAllotC2SaleOrde

from xmdAPI.test_yd_api.process_fuc import getOrderNumber

class TestREALLOTC2SALEORDECase(Base):

    """
    {
  "c2SaleOrderNo": "",
  "salerId": ""
    }

    """
    def test_ReAllotSuccess_emptysalerId(self):

        """测试重新分配工单,分配成功,销售id为空（不校验）@author:Houyanling"""


        ordNo = getOrderNumber(self)

        result = helpReAllotC2SaleOrde(ordNo,
                                       "")

        print(result)

        self.assertEqual(result['code'], 200)

    def test_ReAllot_emptyc2SaleOrderNo(self):

        """测试重新分配工单,分配失败,工单号为空 @author:Houyanling"""

        result = helpReAllotC2SaleOrde("",
                                       "")

        print(result)

        self.assertEqual("分配销售工单失败",result['message'] )

    def test_ReAllot_unusualc2SaleOrderNo(self):

        """测试重新分配工单,分配失败,工单号错误 @author:Houyanling"""

        result = helpReAllotC2SaleOrde("88588899",
                                       ""
                                       )

        print(result)

        self.assertEqual("分配销售工单失败",result['message'] )

