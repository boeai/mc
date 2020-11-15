# 创建订单

from xmdAPI.base import Base

from xmdAPI.test_yd_api.common_fuc import helpCreateOrder

from xmdAPI.test_yd_api.process_fuc import getOrderNumber

from  xmdAPI.test_yd_api.process_fuc import helpXJTG

class xxx(Base):

    def test_Success(self):
        ord = helpXJTG(self)
        print(ord)
