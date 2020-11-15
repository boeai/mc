class OnLineConfig:
    env = 'ONLINE'  # 环境标识
    is_headless = False  # 是否开启静默，True 开启，False 关闭
    to_user = ['@all']  # 企业微信通知名单,个人 域账号，所有人 @all

    home_url = 'https://beijing.m.taoche.com/'
    list_url = 'https://beijing.m.taoche.com/all/'
    sellcar_url = 'https://m.taoche.com/sellcar/directsell.aspx'
    pinggu_url = 'https://m.taoche.com/pinggu/'
    login_url = 'https://passport.m.taoche.com/login/index'
    cardetail_url = 'https://m.taoche.com/buycar/b-dealerydg228073264t.html'
    buycar_url = 'https://beijing.m.taoche.com/all/'
    maiche_url = 'https://m.taoche.com/app/sell'



class TestConfig:
    env = 'TEST'  # 环境标识
    is_headless = False  # 是否开启静默，True 开启，False 关闭
    to_user = ['@all']  # 企业微信通知名单,个人 域账号，所有人 @all

    home_url = 'https://m.taoche.com/'
    zhengzhou_url = 'https://zhengzhou.m.taoche.com/'
    list_url = 'https://beijing.m.taoche.com/all/'
    sellcar_url = 'https://m.taoche.com/sellcar/directsell.aspx'
    pinggu_url = 'https://m.taoche.com/pinggu/'
    login_url = 'https://passport.m.taoche.com/login/index'
    cardetail_url = 'https://m.taoche.com/buycar/b-dealerydg228073264t.html'


config = OnLineConfig()

