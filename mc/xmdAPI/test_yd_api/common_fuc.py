import json
import requests
from xmdAPI.config import config
from xmdAPI.config import URL
import time
# from src.test_xmd import xmd_report_help
# from src.test_xmd import xmd_main_help
import random

header = {'Content-Type': "application/json"}

#
# def xmd_report(suite):
#     """
#     封装report，生成小馬達测试报告，返回报告全路径名称
#     :param suite: 需要进行测试的测试集
#     :return: 返回报告全路径名称
#     """
#     return xmd_report_help.build("XMD", suite)
#
#
# def xmd_send_email(report_full_name):
#     """
#     封装send_email,给测试负责人发送测试报告邮件
#     :param report_full_name: 报告全路径名称
#     :return:
#     """
#     xmd_receivers = xmd_config_help.RECEIVERS
#     xmd_main_help.send_email("XMD", xmd_receivers, report_full_name)


def getHeader():
    header = {'Content-Type': "application/json",
              'Authorization': getToken()}
    return header


# 获得token
def getToken():
    result = helpLogin("wb4001", "uat.portal")
    return result['data']['token']


def getManagerHeader():
    header ={'Content-Type': "application/json",
              'Authorization': getManagerToken()}
    return header


# 获得店长token
def getManagerToken():
    result = helpLogin("10000000367", "uat.portal")
    print("token:" + result['data']['token'])
    return result['data']['token']



# 生成手机号
def setPhoneNumber():
    return random.randint(12300000000, 12400000000)

#获得在售车源
def getFristCar():
    CARLIST = requests.get(config.HOME_URL + URL.TEST_CARLIST_URL,headers=getHeader())
    return CARLIST.json()['data']['content'][0]

#工单详情页
def getGDInfo(orderNO):
    result = requests.get(config.HOME_URL+"/v1/c2-xmd/bss/getOrderDetail?orderNo="+orderNO,headers=getHeader())
    return result.json()

#询价通过
def getXJtg(applyNo):
    requests.get("http://10.6.1.28:8802/task/autoApprove?applyNo="+applyNo)

#订单列表
def getDDList():
    result = requests.get(config.HOME_URL+URL.TEST_ORDERDDLIST_URL,headers=getHeader())
    return result.json()

#获取银行账户
def getBankAccout(orderId):
    result = requests.get(config.HOME_URL+"/v1/cloudorder/cloudStore/orders/detail/"+orderId)
    return result

# 登录
def helpLogin(userName,
              userPwd):
    data = json.dumps({'username': userName,
                       'password': userPwd})
    result = requests.post(config.HOME_URL + URL.TEST_LOGIN_URL, data=data, headers=header).json()
    return result


# 自建工单
def helpZj(clueChannelName, clueChannelId, customerName, customerPhone, purchaseMode, customerType, carCode, gender,
           sparePhone, remark):
    data = json.dumps({'clueChannelName': clueChannelName,
                       'clueChannelId': clueChannelId,
                       'customerName': customerName,
                       'customerPhone': customerPhone,
                       'purchaseMode': purchaseMode,
                       'customerType': customerType,
                       'carCode': carCode,
                       'gender': gender,
                       'sparePhone': sparePhone,
                       'remark': remark,
                       })
    result = requests.post(config.HOME_URL + URL.TEST_ZJ_URL, data=data,
                           headers=getHeader()).json()
    return result

# 重新分配

def helpReAllotC2SaleOrde(c2SaleOrderNo,
                          salerId,
                          ):
    data =json.dumps({'c2SaleOrderNo':c2SaleOrderNo,
                     'salerId':salerId})

    result = requests.post(config.HOME_URL + URL.TEST_ALLOTC2SALEORDE_URL, data=data,
                           headers=getManagerHeader()).json()
    return result


# 工单详情页
# getOrderDetail?isEncrypt=1&orderNo=GD157059077014871
def helpOrderDetail(orderNo):
    result = requests.get(config.HOME_URL + URL.TEST_ORDERDETAIL_URL, data=orderNo,
                          headers=getHeader()).json()
    return result


# 工单列表
# https://p-api-test.kanche.com/v1/c2-xmd/bss/getBssOrders
def helpOrderList(pageIndex, pageSize, workTable,myphone,orderStatusMapping):
    data = json.dumps({'pageIndex': pageIndex,
                       'pageSize': pageSize,
                       'workTable': workTable,
                       'keyWord':myphone,
                       'orderStatusMapping':orderStatusMapping
                       })

    result = requests.post(config.HOME_URL + URL.TEST_ORDERLIST_URL, data=data,
                           headers=getHeader()).json()
    return result


# 添加邀约记录
def helpReserve(carCode,
                followRecordPhotos,
                starLevel,
                taskNo,
                followRecord,
                carStype,
                reservePlace,
                saleOrderNo,
                reserveTime):
    data = json.dumps({'carCode': carCode,
                       'followRecordPhotos': followRecordPhotos,
                       'starLevel': starLevel,
                       'taskNo': taskNo,
                       'followRecord': followRecord,
                       'carStype': carStype,
                       'reservePlace': reservePlace,
                       'saleOrderNo': saleOrderNo,
                       'reserveTime': reserveTime})
    result = requests.post(config.HOME_URL + URL.TEST_REVERSE_URL, data=data,
                           headers=getHeader()).json()
    return result

# 添加接待记录

def helpReceive(approverId,
                approverName,
                arriveShopTime,
                followRecord,
                remark,
                saleOrderNo,
                verificationCode,
                verifyType,
                token,
                taskNo,
                followRecordPhotos,
                receptionType,
                locationLat,
                locationLng,
                locationAddress,
                locationTime):
    data = json.dumps({ "approverId": approverId,
                         "approverName":approverName ,
                         "arriveShopTime":arriveShopTime ,
                         "followRecord":followRecord ,
                         "remark":remark,
                         "saleOrderNo":saleOrderNo ,
                         "verificationCode": verificationCode,
                         "verifyType":verifyType,
                         "token":token ,
                         "taskNo":taskNo,
                         "followRecordPhotos":followRecordPhotos ,
                         "receptionType":receptionType,
                         "locationLat":locationLat,
                         "locationLng":locationLng,
                         "locationAddress": locationAddress,
                         "locationTime":locationTime})

    result = requests.post(config.HOME_URL + URL.TEST_RECEIVE_URL, data=data,
                           headers=getHeader()).json()
    return result


# 添加看车记录
def helpWatchCar(taskNo,
                token,
                resultType,
                carCode,
                signCarFullName,
                saleOrderNo,
                followRecord,
                carSourceType):
    data = json.dumps({'taskNo': taskNo,
                       'token': token,
                       'resultType': resultType,
                       'carCode': carCode,
                       'signCarFullName': signCarFullName,
                       'saleOrderNo': saleOrderNo,
                       'followRecord': followRecord,
                       'carSourceType': carSourceType})
    result = requests.post(config.HOME_URL + URL.TEST_WATCHCAR_URL, data=data,
                           headers=getHeader()).json()
    return result

# 改约记录
def helpNextInvitation(nextInvitationTime,
                       invitationType,
                       saleOrderNo,
                       followRecord,
                       taskNo,
                       token):
    data = json.dumps({'nextInvitationTime': nextInvitationTime,
                       'invitationType': invitationType,
                       'saleOrderNo': saleOrderNo,
                       'followRecord': followRecord,
                       'taskNo': taskNo,
                       'token': token})
    result = requests.post(config.HOME_URL + URL.TEST_NEXTINV_URL, data=data,
                           headers=getHeader()).json()
    return result

#创建询价
def helpCreatXJ(quotePrice,
                financeTheftInsurance,
                downpaymentRatio,
                productId,
                loanPeriod,
                gpsFee,
                insuranceCompanyId,
                insurance,
                storeId,
                customerFinancing,
                orderNo,
                theftInsurance,
                carCode,
                financingProfit,
                customerType,
                paymentMethod,
                carName,
                productName,
                remark,
                insuranceRate,
                customerName):
    data = json.dumps({'quotePrice': quotePrice,
                       'financeTheftInsurance': financeTheftInsurance,
                       'downpaymentRatio': downpaymentRatio,
                       'productId': productId,
                       'loanPeriod': loanPeriod,
                       'gpsFee': gpsFee,
                       'insuranceCompanyId':insuranceCompanyId,
                       'insurance':insurance,
                       'storeId':storeId,
                       'customerFinancing':customerFinancing,
                       'orderNo':orderNo,
                       'theftInsurance':theftInsurance,
                       'carCode':carCode,
                       'financingProfit':financingProfit,
                       'customerType':customerType,
                       'paymentMethod':paymentMethod,
                       'carName':carName,
                       'productName':productName,
                       'remark':remark,
                       'insuranceRate':insuranceRate,
                       'customerName':customerName})
    result = requests.post(config.HOME_URL + URL.TEST_CREATXJ_URL, data=data,
                           headers=getHeader()).json()
    return result

#创建金融单
def helpCreatFinanceOrder(orderNO):
    data = json.dumps({'orderNo':orderNO})
    result = requests.post(config.HOME_URL + URL.TEST_FINANCIAL_URL, data=data,
                           headers=getHeader()).json()

    return result


# 创建订单
def helpCreateOrder(ticketId,
                    createUserId,
                    createUserName,
                    buyerNumber,
                    deposit,
                    remark,
                    mitigationOrderId,
                    eventId,
                    eventEnum,
                    advanceAmount):
    data = json.dumps({'ticketId':ticketId,
                       'createUserId':createUserId,
                       'createUserName':createUserName,
                       'buyerNumber':buyerNumber,
                       'deposit':deposit,
                       'remark':remark,
                       'mitigationOrderId':mitigationOrderId,
                       'eventId':eventId,
                       'eventEnum':eventEnum,
                       'advanceAmount':advanceAmount})

    result =requests.post(config.HOME_URL+URL.TEST_CREATEORDER_URL,data=data,
                            headers=getHeader()).json()

    return result

#创建云店订单
def helpCreateYUNOrder(orderNo,
                       deposit,
                       customerName,
                       remark,
                       customerType,
                       buyerNumber,
                       customerPhone):

    data = json.dumps({'orderNo':orderNo,
                       'deposit':deposit,
                       'customerName':customerName,
                       'remark':remark,
                       'customerType':customerType,
                       'buyerNumber':buyerNumber,
                       'customerPhone':customerPhone})

    result =requests.post(config.HOME_URL+URL.TEST_YUNCREATORDER_URL,data=data,
                            headers=getHeader()).json()

    return result


#申请收款
def helpOfflineTransfer(orderId,
                        payType,
                        transactionSum,
                        transactionForm,
                        useCreditCardPay,
                        isExclusiveAccount,
                        transactionType):

    data = json.dumps({'orderId':orderId,
                       'payType':payType,
                       'transactionSum':transactionSum,
                       'transactionForm':transactionForm,
                       'useCreditCardPay':useCreditCardPay,
                       'isExclusiveAccount':isExclusiveAccount,
                       'transactionType':transactionType})

    result =requests.post(config.HOME_URL+URL.TEST_APPLYTRANSFER_URL,data=data,
                            headers=getHeader()).json()

    return result


'''
{
    "orderId":"201903060001",
    "partyAName":"小王",
    "partyAIdCard":"123456789098765",
    "partyAContactsName":"小王",
    "partyAPhone":"15910521111",
    "partyAAddress":"小王村",
    "carName":"大众甲壳虫2018款3.0T自动舒适版",
    "vinCode":"ENM2991LHK",
    "buyCarType":1,
    "dealPrice":"3000000",
    "advanceChargePrice":"2989988999",
    "storageChargePrice":"500",
    "firstPaymentPrice":"30000"
}
'''
#订单-电子签（采购协议）
def helpEntruePurchase(orderId,
                       partyAName,
                       partyAIdCard,
                       partyAContactsName,
                       partyAPhone,
                       partyAAddress,
                       carName,
                       vinCode,
                       buyCarType,
                       dealPrice,
                       advanceChargePrice,
                       storageChargePrice,
                       firstPaymentPrice):

    data = json.dumps({'orderId':orderId,
                       'partyAName':partyAName,
                       'partyAIdCard':partyAIdCard,
                       'partyAContactsName':partyAContactsName,
                       'partyAPhone':partyAPhone,
                       'partyAAddress':partyAAddress,
                       'carName':carName,
                       'vinCode':vinCode,
                       'buyCarType':buyCarType,
                       'dealPrice':dealPrice,
                       'advanceChargePrice':advanceChargePrice,
                       'storageChargePrice':storageChargePrice,
                       'firstPaymentPrice':firstPaymentPrice})

    result =requests.post(config.HOME_URL+URL.TEST_ENTUREPURCHASE_URL,data=data,
                            headers=getHeader()).json()

    return result


# 订单-电子签（车辆交接确认函）
'''
    
    {
	"partyBIdCard": "2939393993",
	"carName": "Audi Sport 2017款 2.5T Limousine",
	"partyAName": "18101554260",
	"carTransferDate": "2019-12-24",
	"vinCode": "EZKVHFRP5C26D5YM0",
	"partyAPhone": "18101554260",
	"partyBPhone": "18164664999",
	"signDate": "2019-11-26",
	"orderId": "20191124752483",
	"remark": "嗯嗯对",
	"partyAIdCard": "22072418880201262565",
	"entrustPurchaseContractId": "QY2019112400824",
	"subsidiaryData": "内心的那女的",
	"partyBName": "看看"
    }
'''
def helpHandoverConfirm(partyBIdCard,
                        carName,
                        partyAName,
                        carTransferDate,
                        vinCode,
                        partyAPhone,
                        partyBPhone,
                        signDate,
                        orderId,
                        remark,
                        partyAIdCard,
                        entrustPurchaseContractId,
                        subsidiaryData,
                        partyBName):
    data = json.dumps({'partyBIdCard': partyBIdCard,
                       'carName': carName,
                       'partyAName': partyAName,
                       'carTransferDate': carTransferDate,
                       'vinCode': vinCode,
                       'partyAPhone': partyAPhone,
                       'partyBPhone': partyBPhone,
                       'signDate':signDate,
                       'orderId': orderId,
                       'remark': remark,
                       'partyAIdCard': partyAIdCard,
                       'entrustPurchaseContractId': entrustPurchaseContractId,
                       'subsidiaryData': subsidiaryData,
                       'partyBName': partyBName})

    result = requests.post(config.HOME_URL + URL.TEST_HANDOVERCONFIRM_URL, data=data,
                           headers=getHeader()).json()
    return result


# 订单-线下签（车辆交接确认函）
def helpSignoffline(orderId,
                    make,
                    model,
                    latitude,
                    cdn,
                    source,
                    longitude,
                    type):
    images = [{'make': make,
               'model': model,
               'latitude': latitude,
               'cdn': cdn,
               'source': source,
               'longitude': longitude}]
    data = json.dumps({'orderId': orderId,
                       'images': images,
                       'type': type})
    result = requests.post(config.HOME_URL + URL.TEST_PAPERSIGN_URL, data=data,
                           headers=getHeader()).json()
    return result


# 订单-电子签（保真协议）
def helpEnsureReal(carMileage,
                   orderId,
                   partyAPhone,
                   carName,
                   agreementTakeEffectDate,
                   partyAName,
                   vinCode,
                   partyAIdCard,
                   dealPrice,
                   type):


    data = json.dumps({'carMileage': carMileage,
                       'orderId': orderId,
                       'partyAPhone': partyAPhone,
                       'carName': carName,
                       'agreementTakeEffectDate': agreementTakeEffectDate,
                       'partyAName':partyAName,
                       'vinCode': vinCode,
                       'partyAIdCard': partyAIdCard,
                       'dealPrice': dealPrice,
                       'type':type
                       })

    result =requests.post(config.HOME_URL+URL.TEST_ENSUREREAL_URL,data=data,
                            headers=getHeader()).json()

    return result