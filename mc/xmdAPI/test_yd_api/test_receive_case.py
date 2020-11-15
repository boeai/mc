#添加接待记录case

# -*- coding=UTF-8 -*-

from xmdAPI.base import Base

from xmdAPI.test_yd_api.common_fuc import helpReceive

from xmdAPI.test_yd_api.process_fuc import getOrderNumber

class TestRECEIVECase(Base):

    """
    无验证码请求参数：

    {
	"verifyType": "0",
	"approverName": "云店1销售云店1车务",
	"followRecordPhotos": ["https://optimize-qa.kanche.com/merchant/basic_inf/b41c184d1fbd0bb01ca63006983976d0.jpg"],
	"followRecord": "添加接待记录",
	"taskNo": "TX157257447016885",
	"receptionType": 2,
	"saleOrderNo": "GD157257426044883",
	"locationLat": "39.917174",
	"token": "42bb5122483c4faeb21c468c7c6001cf",
	"locationAddress": "北京市西城区二七剧场路7号",
	"approverId": "06ed0775dbc84eb9b67bb3de7c9ed88d",
	"locationTime": "2019-11-01 10:15:45",
	"locationLng": "116.352497"
    }
    """

    def test_ReceiveSuccess(self):

        """测试添加接待记录接口,添加接待记录成功（无验证码接待）,@author:Houyanling"""

        ordNo = getOrderNumber(self)

        result = helpReceive(
                             "",
                             "云店1销售云店1车务",
                             "",
                             "添加接待记录",
                             "",
                             ordNo,
                             "",
                             "0",
                             "42bb5122483c4faeb21c468c7c6001cf",
                             "TX157257447016885",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             2,
                             "39.917174",
                             "116.352497",
                             "北京市西城区二七剧场路7号",
                             "2019-11-01 10:15:45")
        print(result)

        self.assertEqual(result['code'], 200)

    def test_ReceiveFail_unusuallocationTime(self):

        """测试添加接待记录接口,添加接待记录成功 locationTime为空，不校验（无验证码接待）,@author:Houyanling"""

        ordNo = getOrderNumber(self)

        result = helpReceive("",
                             "云店1销售云店1车务",
                             "",
                             "添加接待记录",
                             "",
                             ordNo,
                             "",
                             "0",
                             "42bb5122483c4faeb21c468c7c6001cf",
                             "TX157257447016885",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             2,
                             "39.917174",
                             "116.352497",
                             "",
                             "dddeee"
                             )

        print(result)

        self.assertEqual(result['code'],200)

    def test_Receive_emptyapproverName(self):

        """测试添加接待记录接口,添加接待记录失败，审批人为空（无验证码接待）,@author:Houyanling"""

        ordNo=getOrderNumber(self)

        result = helpReceive("",
                             "",
                             "",
                             "添加接待记录",
                             "",
                             ordNo,
                             "",
                             "0",
                             "42bb5122483c4faeb21c468c7c6001cf",
                             "TX157257447016885",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             2,
                             "39.917174",
                             "116.352497",
                             "北京市西城区二七剧场路7号",
                             "2019-11-01 10:15:45"
                              )
        print(result)

        self.assertEqual(result['message'], "审批人不能为空")


    def test_ReceiveFail_emptyfollowRecordPhotos(self):

        """测试添加接待记录接口,添加接待记录失败，followRecordPhotos为空（无验证码接待）,@author:Houyanling"""

        ordNo = getOrderNumber(self)

        result = helpReceive(
                             "",
                             "云店1销售云店1车务",
                             "",
                             "添加接待记录",
                             "",
                             ordNo,
                             "",
                             "0",
                             "42bb5122483c4faeb21c468c7c6001cf",
                             "TX157257447016885",
                             "",
                             2,
                             "",
                             "",
                             "北京市西城区二七剧场路7号",
                             "2019-11-01 10:15:45")
        self.assertEqual(result['error'], "Bad Request")

    def test_ReceiveFail_unusualfollowRecordPhotos(self):
        """测试添加接待记录接口,添加接待记录失败，followRecordPhotos异常（无验证码接待）,@author:Houyanling"""

        ordNo = getOrderNumber(self)

        result = helpReceive( "",
                             "云店1销售云店1车务",
                             "",
                             "添加接待记录",
                             "",
                             ordNo,
                             "",
                             "0",
                             "42bb5122483c4faeb21c468c7c6001cf",
                             "TX157257447016885",
                             "这个是接待凭证",
                             2,
                             "39.917174",
                             "116.352497",
                             "北京市西城区二七剧场路7号",
                             "2019-11-01 10:15:45")


        self.assertEqual(result['error'],"Bad Request")

    def test_ReceiveFail_emptysaleOrderNo(self):

        """测试添加接待记录接口,添加接待记录失败，saleOrderNo为空（无验证码接待）,@author:Houyanling"""

        result = helpReceive( "",
                             "云店1销售云店1车务",
                             "",
                             "添加接待记录",
                             "",
                             "",
                             "",
                             "0",
                             "42bb5122483c4faeb21c468c7c6001cf",
                             "TX157257447016885",
                            ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             2,
                             "39.917174",
                             "116.352497",
                             "北京市西城区二七剧场路7号",
                             "2019-11-01 10:15:45")
        print(result)
        self.assertIn("销售工单单号信息不能为空",result['message'] )


    def test_ReceiveFail_unusualsaleOrderNo(self):

        """测试添加接待记录接口,添加接待记录失败，saleOrderNo异常（无验证码接待）,@author:Houyanling"""

        result = helpReceive("",
                             "云店1销售云店1车务",
                             "",
                             "添加接待记录",
                             "",
                             "GD123411111",
                             "",
                             "0",
                             "42bb5122483c4faeb21c468c7c6001cf",
                             "TX157257447016885",
                            ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             2,
                             "39.917174",
                             "116.352497",
                             "北京市西城区二七剧场路7号",
                             "2019-11-01 10:15:45"
                             )

        print(result)
        self.assertIn(result['message'], "添加接待记录异常")

    def test_ReceiveFail_emptyfollowRecord(self):

        """测试添加接待记录接口,添加接待记录失败，followRecord为空（无验证码接待）,@author:Houyanling"""
        ordNo = getOrderNumber(self)

        result = helpReceive("",
                             "云店1销售云店1车务",
                             "",
                             "",
                             "",
                             ordNo,
                             "",
                             "0",
                             "42bb5122483c4faeb21c468c7c6001cf",
                             "TX157257447016885",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             2,
                             "39.917174",
                             "116.352497",
                             "北京市西城区二七剧场路7号",
                             "2019-11-01 10:15:45"
                            )

        print(result)

        self.assertEqual(result['message'],"跟进纪录不能为空")

    def test_ReceiveFail_emptylocationAddress(self):

        """测试添加接待记录接口,添加接待记录失败，locationAddress为空（无验证码接待）,@author:Houyanling"""

        ordNo =getOrderNumber(self)

        result=helpReceive("",
                             "云店1销售云店1车务",
                             "",
                             "添加接待记录",
                             "",
                             ordNo,
                             "",
                             "0",
                             "42bb5122483c4faeb21c468c7c6001cf",
                             "TX157257447016885",
                             ["https://images-qa.kanche.com/merchant/basic_inf/d6082bc38577c4b6a5b7acaaf8d61b5b.jpg"],
                             2,
                             "39.917174",
                             "116.352497",
                             "",
                             "2019-11-01 10:15:45"
                              )

        print(result)

        self.assertEqual(result['message'],"地址不能为空")
