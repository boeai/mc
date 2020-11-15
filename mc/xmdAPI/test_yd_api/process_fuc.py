from xmdAPI.test_yd_api.test_zj_case import TestZJCase
from xmdAPI.test_yd_api.test_orderList_case import TestORDERLISTCase
from xmdAPI.test_yd_api.common_fuc import helpWatchCar
from xmdAPI.test_yd_api.common_fuc import getFristCar
from xmdAPI.test_yd_api.common_fuc import helpCreatXJ
from xmdAPI.test_yd_api.common_fuc import getXJtg
from xmdAPI.test_yd_api.common_fuc import getGDInfo
import datetime

#创建工单接口
def getOrderNumber(self):
    # 自建工单
    zj_phone = TestZJCase.get_zj_phone(self)
    print(zj_phone)
    # 通过手机号查询工单
    orderList = TestORDERLISTCase.test_getListSuccess(self,str(zj_phone))
    orderNumber = orderList['data']['c2Orders'][0]['orderNo']

    return orderNumber

#获取时间接口
def getTime(time_what):
    timeW = datetime.datetime.now()
    if(time_what == 'yesterday'):
        timeW = timeW + datetime.timedelta(days=-1)
        return timeW.strftime('%Y-%m-%d %H:%M:%S')
    elif(time_what == 'today'):
        return timeW.strftime('%Y-%m-%d %H:%M:%S')
    elif(time_what == 'tomorrow'):
        timeW = timeW + datetime.timedelta(days=1)
        return timeW.strftime('%Y-%m-%d %H:%M:%S')
    else:
        timeW = timeW + datetime.timedelta(days=31)
        return timeW.strftime('%Y-%m-%d %H:%M:%S')


def helpWatchcarSuccess(self,carcode):
    """测试添加看车记录接口,添加看车记录成功,@author:liusai"""
    ordNo = getOrderNumber(self)
    helpWatchCar('txfdkslfjdskfjdl',
                 '2ewrew',
                 '1',
                 carcode,
                 '奥迪RS 3-2017款2017款 2.5T Limousine',
                 ordNo,
                 '就觉得亟待解决的家我是备注哈哈哈哈',
                 '0')
    return ordNo

def helpXJTG(self):
    carInfo = getFristCar()
    carcode = carInfo['id']
    carPrice = str(carInfo['price']['quotedPrice'])
    orderNO = helpWatchcarSuccess(self,carcode)
    helpCreatXJ(carPrice,
                True,
                '50',
                'M000325',
                '36',
                '1500',
                '2',
                '1300',
                '265895',
                '1200',
                orderNO,
                '1000',
                carcode,
                '1100',
                1,
                2,
                '日产 天籁 2010 2010款 2.0L XL 周年纪念版',
                '暖鑫融二手车常规淘车V',
                '对大家都觉得亟待解决的跟进记录',
                '35',
                '19920203016')

    applyNo = getGDInfo(orderNO)
    getXJtg(applyNo['data']['applyNo'])
    return orderNO

