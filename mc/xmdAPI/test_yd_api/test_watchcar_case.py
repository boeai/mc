#添加看车记录case
from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpWatchCar
from xmdAPI.test_yd_api.process_fuc import getOrderNumber


class TestWATCHCARCase(Base):
    '''
    {
        taskNo,
        token,
        "token":""
    	"resultType": "1",
    	"carCode": "001553731",
    	"signCarFullName": "奥迪RS 3-2017款2017款 2.5T Limousine",
    	"saleOrderNo": "GD157259183473824",
    	"followRecord": "就觉得亟待解决的家",
    	"carSourceType": "0"

    }
    '''

    def test_watchcarSuccess(self):
        """测试添加看车记录接口,添加看车记录成功,@author:liusai"""
        ordNo = getOrderNumber(self)
        result = helpWatchCar('txfdkslfjdskfjdl',
                              '2ewrew',
                              '1',
                              '001553731',
                              '奥迪RS 3-2017款2017款 2.5T Limousine',
                              ordNo,
                              '就觉得亟待解决的家我是备注哈哈哈哈',
                              '0')
        self.assertEqual(result['code'],200)


    def test_watchcarSuccess_taskNoEmpty(self):
        """测试添加看车记录接口,添加看车记录成功，taskNo为空，不校验,@author:liusai"""
        ordNo = getOrderNumber(self)
        result = helpWatchCar('',
                              '2ewrew',
                              '1',
                              '001553731',
                              '奥迪RS 3-2017款2017款 2.5T Limousine',
                              ordNo,
                              '就觉得亟待解决的家我是备注哈哈哈哈',
                              '0')
        self.assertEqual(result['code'],200)

    def test_watchcarSuccess_tokenEmpty(self):
        """测试添加看车记录接口,添加看车记录成功，token为空，不校验,@author:liusai"""
        ordNo = getOrderNumber(self)
        result = helpWatchCar('fdsfdsfda',
                              '',
                              '1',
                              '001553731',
                              '奥迪RS 3-2017款2017款 2.5T Limousine',
                              ordNo,
                              '就觉得亟待解决的家我是备注哈哈哈哈',
                              '0')
        self.assertEqual(result['code'],200)

    def test_watchcarSuccess_signCarFullNameEmpty(self):
        """测试添加看车记录接口,添加看车记录成功，signCarFullName为空，不校验,@author:liusai"""
        ordNo = getOrderNumber(self)
        result = helpWatchCar('fdsfdsfda',
                              'erewr',
                              '1',
                              '001553731',
                              '奥迪RS 3-2017款2017款 2.5T Limousine',
                              ordNo,
                              '',
                              '0')
        self.assertEqual(result['code'],200)

    def test_watchcarSuccess_followRecordEmpty(self):
        """测试添加看车记录接口,添加看车记录成功，followRecord为空，不校验,@author:liusai"""
        ordNo = getOrderNumber(self)
        result = helpWatchCar('fdsfdsfda',
                              'erewr',
                              '1',
                              '001553731',
                              '奥迪RS 3-2017款2017款 2.5T Limousine',
                              ordNo,
                              '',
                              '0')
        self.assertEqual(result['code'], 200)


    def test_watchcarSuccess_carSourceTypeEmpty(self):
        """测试添加看车记录接口,添加看车记录成功，carSourceType为空，不校验,@author:liusai"""
        ordNo = getOrderNumber(self)
        result = helpWatchCar('fdsfdsfda',
                              'erewr',
                              '1',
                              '001553731',
                              '奥迪RS 3-2017款2017款 2.5T Limousine',
                              ordNo,
                              '就觉得亟待解决的家我是备注哈哈哈哈',
                              '')
        self.assertEqual(result['code'], 200)

    def test_watchcarFail_saleOrderNoEmpty(self):
        """测试添加看车记录接口,添加看车记录失败，taskNo为空，不校验,@author:liusai"""
        result = helpWatchCar('fdsfdsfdsfs',
                              '2ewrew',
                              '1',
                              '001553731',
                              '奥迪RS 3-2017款2017款 2.5T Limousine',
                              '',
                              '就觉得亟待解决的家我是备注哈哈哈哈',
                              '0')
        self.assertIn("销售工单单号信息不能为空",result['message'])


    def test_watchcarSuccess_carCodeEmpty(self):
        """测试添加看车记录接口,添加看车记录失败，carcode为空,@author:liusai"""
        ordNo = getOrderNumber(self)
        result = helpWatchCar('fdsfdsfda',
                              'fdsfds',
                              '1',
                              '',
                              '奥迪RS 3-2017款2017款 2.5T Limousine',
                              ordNo,
                              '就觉得亟待解决的家我是备注哈哈哈哈',
                              '0')
        self.assertIn("签约车源唯一码不能为空",result['message'])

    def test_watchcarFail_resultTypeEmpty(self):
        """测试添加看车记录接口,添加看车记录失败，resultType(带看结果)为空，,@author:liusai"""
        ordNo = getOrderNumber(self)
        result = helpWatchCar('fdsfdsfda',
                              'fsdfds',
                              '',
                              '001553731',
                              '奥迪RS 3-2017款2017款 2.5T Limousine',
                              ordNo,
                              '就觉得亟待解决的家我是备注哈哈哈哈',
                              '0')
        self.assertIn("带看结果不能为空",result['message'])