#改约记录case（改约，改接待）

from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpNextInvitation
from xmdAPI.test_yd_api.process_fuc import getOrderNumber
from xmdAPI.test_yd_api.process_fuc import getTime

class TESTNEXTINVTATIONCASE(Base):
    '''
    {
	"nextInvitationTime": "2019-11-03 13:00:42",
	"invitationType": "1",(1改约，2改接待)
	"saleOrderNo": "GD157266848321652",
	"followRecord": "我是跟进记录哈哈哈哈哈哈哈",
	"taskNo": "TX157266848334653",
	"token": "99d32225054942bda37e47f1c4f811a4"
    }
    '''

    def test_nextInvSuccess_nextInvitationOld(self):
        """测试添加改约接口,添加改约记录成功,nextInvitation时间为前一天，@author:liusai"""
        ordNo = getOrderNumber(self)
        cTime = getTime('yesterday')
        result = helpNextInvitation(cTime,
                                    '1',
                                    ordNo,
                                    '我是跟进记录哈哈哈哈',
                                    'txjdjjdd',
                                    'eeekeekekek')
        self.assertEqual(result['code'],200)

    def test_nextInvSuccess_followRecordEmptyl(self):
        """测试添加改约接口,添加改约记录成功,followRecord为空，@author:liusai"""
        ordNo = getOrderNumber(self)
        cTime = getTime('tomorrow')
        result = helpNextInvitation(cTime,
                                    '2',
                                    ordNo,
                                    '',
                                    'txjdjjdd',
                                    'eeekeekekek')
        self.assertEqual(result['code'], 200)

    def test_nextInvFail_nextInvitationEmpty(self):
        """测试添加改约接口,添加改约记录失败,nextInvitation为空，@author:liusai"""
        ordNo = getOrderNumber(self)
        result = helpNextInvitation('',
                                    '1',
                                    ordNo,
                                    '我是跟进记录哈哈哈哈',
                                    'txjdjjdd',
                                    'eeekeekekek')
        self.assertIn(result['message'],"改约异常")

    def test_nextInvFail_nextInvitationBig(self):
        """测试添加改约接口,添加改约记录失败,nextInvitation为30天后，@author:liusai"""
        ordNo = getOrderNumber(self)
        cTime = getTime('month')
        result = helpNextInvitation(cTime,
                                    '1',
                                    ordNo,
                                    '我是跟进记录哈哈哈哈',
                                    'txjdjjdd',
                                    'eeekeekekek')
        self.assertIn('改约时间必须为当前时间的30天以内',result['message'])

    def test_nextInvFail_invitationTypeEmpty(self):
        """测试添加改约接口,添加改约记录失败,invitationType为空，@author:liusai"""
        ordNo = getOrderNumber(self)
        cTime = getTime('tomorrow')
        result = helpNextInvitation(cTime,
                                    '',
                                    ordNo,
                                    '我是跟进记录哈哈哈哈',
                                    'txjdjjdd',
                                    'eeekeekekek')
        self.assertIn('改约类型不能为空',result['message'])

    def test_nextInvFail_invitationTypeUnusual(self):
        """测试添加改约接口,添加改约记录失败,invitationType非12，@author:liusai"""
        ordNo = getOrderNumber(self)
        cTime = getTime('tomorrow')
        result = helpNextInvitation(cTime,
                                    '0',
                                    ordNo,
                                    '我是跟进记录哈哈哈哈',
                                    'txjdjjdd',
                                    'eeekeekekek')
        self.assertIn('接待类型参数有误',result['message'])

    def test_nextInvFail_saleOrderNoEmpty(self):
        """测试添加改约接口,添加改约记录失败,saleOrderNo为空，@author:liusai"""
        ordNo = getOrderNumber(self)
        cTime = getTime('tomorrow')
        result = helpNextInvitation(cTime,
                                    '1',
                                    '',
                                    '我是跟进记录哈哈哈哈',
                                    'txjdjjdd',
                                    'eeekeekekek')
        self.assertIn('销售工单单号信息不能为空',result['message'])

    def test_nextInvFail_saleOrderNoUnusual(self):
        """测试添加改约接口,添加改约记录失败,saleOrderNo异常，@author:liusai"""
        ordNo = getOrderNumber(self)
        cTime = getTime('tomorrow')
        result = helpNextInvitation(cTime,
                                    '2',
                                    'fdjsfdjklsfjdjfdskfjks',
                                    '我是跟进记录哈哈哈哈',
                                    'txjdjjdd',
                                    'eeekeekekek')
        self.assertIn('无此工单号',result['message'])

