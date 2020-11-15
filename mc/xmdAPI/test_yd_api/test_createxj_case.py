#添加创建询价case

from xmdAPI.base import  Base
from xmdAPI.test_yd_api.common_fuc import helpCreatXJ
from xmdAPI.test_yd_api.process_fuc import getOrderNumber
from xmdAPI.test_yd_api.process_fuc import helpWatchcarSuccess
from xmdAPI.test_yd_api.common_fuc import getFristCar


from xmdAPI.test_yd_api.process_fuc import getTime

carInfo = getFristCar()
carcode = carInfo['id']
carPrice = str(carInfo['price']['quotedPrice'])


class TestCREATXJCase(Base):
    '''
    {
	"quotePrice": "25000",
	"financeTheftInsurance": true,
	"downpaymentRatio": "50",
	"productId": "M000325",
	"loanPeriod": "36",
	"gpsFee": "1500",
	"insuranceCompanyId": 2,
	"insurance": "1300",
	"storeId": "265895",
	"customerFinancing": "1200",
	"orderNo": "GD157267433886612",
	"theftInsurance": "1000",
	"carCode": "020969510",
	"financingProfit": "1100",
	"customerType": 1,
	"paymentMethod": 2,
	"carName": "日产 天籁 2010 2010款 2.0L XL 周年纪念版",
	"productName": "暖鑫融二手车常规淘车V",
	"remark": "对大家都觉得亟待解决的跟进记录",
	"insuranceRate": "35",
	"customerName": "19920203016"
    }
    '''
    def test_creatxjSuccess(self):
        """测试添加創建詢價接口,添加詢價成功，@author:liusai"""
        ordNo = helpWatchcarSuccess(self, carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
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
        self.assertEqual(result['code'],200)

    def test_creatxjSuccess_financeTheftInsuranceEmpty(self):
        """测试创建询价接口,创建询价成功，financeTheftInsurance為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             '',
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
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
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_downpaymentRatioEmpty(self):
        """测试创建询价接口,创建询价成功，downpaymentRatio為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
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
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_loanPeriodEmpty(self):
        """测试创建询价接口,创建询价成功，loanPeriod為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             '',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
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
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_gpsFeeEmpty(self):
        """测试创建询价接口,创建询价成功，gpsFee為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
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
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_insuranceCompanyIdEmpty(self):
        """测试创建询价接口,创建询价成功，insuranceCompanyId為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
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
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_insuranceEmpty(self):
        """测试创建询价接口,创建询价成功，insurance為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '',
                             '265895',
                             '1200',
                             ordNo,
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
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_storeIdEmpty(self):
        """测试创建询价接口,创建询价成功，storeId為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '',
                             '1200',
                             ordNo,
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
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_customerFinancingEmpty(self):
        """测试创建询价接口,创建询价成功，customerFinancing為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '',
                             ordNo,
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
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_theftInsuranceEmpty(self):
        """测试创建询价接口,创建询价成功，theftInsurance為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
                             '',
                             carcode,
                             '1100',
                             1,
                             2,
                             '日产 天籁 2010 2010款 2.0L XL 周年纪念版',
                             '暖鑫融二手车常规淘车V',
                             '对大家都觉得亟待解决的跟进记录',
                             '35',
                             '19920203016')
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_financingProfitEmpty(self):
        """测试创建询价接口,创建询价成功，financingProfit為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
                             '1000',
                             carcode,
                             '',
                             1,
                             2,
                             '日产 天籁 2010 2010款 2.0L XL 周年纪念版',
                             '暖鑫融二手车常规淘车V',
                             '对大家都觉得亟待解决的跟进记录',
                             '35',
                             '19920203016')
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_customerTypeEmpty(self):
        """测试创建询价接口,创建询价成功，customerType為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
                             '1000',
                             carcode,
                             '1100',
                             '',
                             2,
                             '日产 天籁 2010 2010款 2.0L XL 周年纪念版',
                             '暖鑫融二手车常规淘车V',
                             '对大家都觉得亟待解决的跟进记录',
                             '35',
                             '19920203016')
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_paymentMethodEmpty(self):
        """测试创建询价接口,创建询价成功，paymentMethod為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
                             '1000',
                             carcode,
                             '1100',
                             '1',
                             '',
                             '日产 天籁 2010 2010款 2.0L XL 周年纪念版',
                             '暖鑫融二手车常规淘车V',
                             '对大家都觉得亟待解决的跟进记录',
                             '35',
                             '19920203016')
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_carNameEmpty(self):
        """测试创建询价接口,创建询价成功，carName為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
                             '1000',
                             carcode,
                             '1100',
                             1,
                             2,
                             '',
                             '暖鑫融二手车常规淘车V',
                             '对大家都觉得亟待解决的跟进记录',
                             '35',
                             '19920203016')
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_productNameEmpty(self):
        """测试创建询价接口,创建询价成功，productName為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
                             '1000',
                             carcode,
                             '1100',
                             1,
                             2,
                             '日产 天籁 2010 2010款 2.0L XL 周年纪念版',
                             '',
                             '对大家都觉得亟待解决的跟进记录',
                             '35',
                             '19920203016')
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_remarkEmpty(self):
        """测试创建询价接口,创建询价成功，remark為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
                             '1000',
                             carcode,
                             '1100',
                             1,
                             2,
                             '日产 天籁 2010 2010款 2.0L XL 周年纪念版',
                             '暖鑫融二手车常规淘车V',
                             '',
                             '35',
                             '19920203016')
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_insuranceRateEmpty(self):
        """测试创建询价接口,创建询价成功，insuranceRate為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
                             '1000',
                             carcode,
                             '1100',
                             1,
                             2,
                             '日产 天籁 2010 2010款 2.0L XL 周年纪念版',
                             '暖鑫融二手车常规淘车V',
                             '对大家都觉得亟待解决的跟进记录',
                             '',
                             '19920203016')
        self.assertEqual(result['code'], 200)

    def test_creatxjSuccess_customerNameEmpty(self):
        """测试创建询价接口,创建询价成功，customerName為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
                             '1000',
                             carcode,
                             '1100',
                             1,
                             2,
                             '日产 天籁 2010 2010款 2.0L XL 周年纪念版',
                             '暖鑫融二手车常规淘车V',
                             '对大家都觉得亟待解决的跟进记录',
                             '35',
                             '')
        self.assertEqual(result['code'], 200)

    def test_creatxjFail_quotePriceEmpty(self):
        """测试创建询价接口,创建询价失敗，quotePrice為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ('',
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
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
        self.assertIn("所询价格不能超过或低于展示价格的30",result['message'])

    def test_creatxjFail_productIdEmpty(self):
        """测试创建询价接口,创建询价失敗，productId為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
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
        print(result)
        self.assertIn("分期购车未传金融产品",result['message'])

    def test_creatxjFail_orderNoEmpty(self):
        """测试创建询价接口,创建詢價失敗，orderNo為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             '',
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
        self.assertIn("创建询价申请失败", result['message'])

    def test_creatxjFail_carcodeEmpty(self):
        """测试创建询价接口,创建詢價失敗，carcode為空，@author:liusai"""
        ordNo = helpWatchcarSuccess(self,carcode)
        result = helpCreatXJ(carPrice,
                             True,
                             '50',
                             'M000325',
                             '36',
                             '1500',
                             '2',
                             '1300',
                             '265895',
                             '1200',
                             ordNo,
                             '1000',
                             '',
                             '1100',
                             1,
                             2,
                             '日产 天籁 2010 2010款 2.0L XL 周年纪念版',
                             '暖鑫融二手车常规淘车V',
                             '对大家都觉得亟待解决的跟进记录',
                             '35',
                             '19920203016')
        self.assertIn("车源状态为在售时才能发起询价", result['message'])