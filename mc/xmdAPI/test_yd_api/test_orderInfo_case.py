#工单详情页case

from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpOrderDetail


class TestORDERINFOCase(Base):

    def test_getSuccess(self):
        #自建工单
        #跟进手机号获取工单列表
        """测试工单详情页接口,成功，正确工单号,@author:liusai"""
        result = helpOrderDetail("GD156974124870815")
        print(result)