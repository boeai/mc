class OnLineConfig:
    env = 'ONLINE'  # 环境标识
    is_headless = False  # 是否开启静默，True 开启，False 关闭
    to_user = ['@all']  # 企业微信通知名单,个人 域账号，所有人 @all


    home_url = 'https://beijing.taoche.com/'
    bj_buycar_url = 'https://beijing.taoche.com/all/'
    news_url = 'https://news.taoche.com/home/'
    pinggu_url = 'https://www.taoche.com/pinggu/'
    bugcar_url = 'https://zhengzhou.taoche.com/all/'
    beijing_buycar_url ='https://beijing.taoche.com/all'
    buycar_collect_url='https://www.taoche.com/buycar/b-dealermd232450832t.html?source=2808'
    brand_name = '宝马'


class TestConfig:
    env = 'TEST'  # 环境标识
    is_headless = False  # 是否开启静默，True 开启，False 关闭
    to_user = ['@all']  # 企业微信通知名单

    home_url = 'https://www.taoche.com'
    news_url = 'https://news.taoche.com/home/'
    pinggu_url = 'https://www.taoche.com/pinggu/'
    bugcar_url = 'https://zhengzhou.taoche.com/all/'
    buycar_collect_url = 'https://www.taoche.com/buycar/b-dealermd232450832t.html?source=2808'
    brand_name = '宝马'


config = OnLineConfig()
