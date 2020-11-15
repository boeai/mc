class OnLineConfig:
    env = 'ONLINE'  # 环境标识
    to_user = ['@all']  # 企业微信通知名单,个人 域账号，所有人 @all

    appium_service = 'http://localhost:4723/wd/hub'
    # OPPO R11 P
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7.1.1',
        'deviceid': '93c0dcb8',
        'deviceName': 'OPPO R11 Plusk',
        'appPackage': 'com.ucar.app',
        'appActivity': 'com.ucar.app.activity.home.AppstartActivity',
        'noReset': True,  # true:不重新安装APP，false:重新安装app
        'noSign': True,
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }


class TestConfig:
    env = 'TEST'  # 环境标识
    to_user = ['@all']  # 企业微信通知名单,个人 域账号，所有人 @all

    appium_service = 'http://localhost:4723/wd/hub'
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7.1.1',
        'deviceid': '93c0dcb8',
        'deviceName': 'OPPO R11 Plusk',
        'appPackage': 'com.ucar.app',
        'appActivity': 'com.ucar.app.activity.home.AppstartActivity',
        'noReset': True,  # true:不重新安装APP，false:重新安装app
        'noSign': True,
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }


config = OnLineConfig()


