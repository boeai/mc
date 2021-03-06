class HeaderLocator:

    HEADER_BAR = ('class', 'shortcut')
    TC_HOME = ('xpath', "/html/body/div[@class='shortcut']/div/div/a")

    HEADER_SEARCH = ('class', 'tc-header')
    LOGO = ('class', 'logo')
    CITY_CONTROL = ('class', 'city-name')
    SEARCH_TAB = ('class', 'search-tab')
    SEARCH_ERSHOUCHE = ('id', 'tc_search_ershoucheTab')
    SEARCH_ERSHOUCHE_TEXT = ('id', 'tc_search_txtErshouche')
    SEARCH_NEWCAR = ('id', 'tc_search_newcarTab')
    SEARCH_NEWCAR_TEXT = ('id', 'tc_search_txtNewcar')
    SEARCH_BTN = ('id', 'tc_search_btnErshouche')

    HEADER_NAV = ('class', 'nav_menu')
    NAV_MENU = ('id', 'ul_menu')
    NAV_DEFAULT = ('css', '#ul_menu > li.home.current')
    NAV_BUYCAR = ('id', 'tc_top_liMenuErshouche')
    NAV_SELLCAR = ('xpath', '//*[@id="ul_menu"]/li[3]')
    BJAD = ('xpath', '//*[@id="div_10ea55d7-74ca-4392-b785-e097565cb1c2"]/div[1]/a/img')
    BZAD = ('xpath','/html/body/div[8]/div[2]/div[1]')
    Ibuycar = ('xpath','/html/body/div[8]/div[1]/div/a')
    BJbuycar = ('xpath','/html/body/div[8]/div[1]/div/span[2]/a')
    Car_price = ('xpath','//*[@id="divScreen"]/li[2]/a[4]')
    bz_tag = ('xpath','//*[@id="container_base"]/ul/li[1]/div[2]/div[2]/em')
    brand_name = ('xpath','//*[@id="divScreen"]/li[1]/a[1]/span')
    Price_path = ('xpath','//*[@id="containerId"]/div[1]/div[1]/ul/li[1]/a')
    Car_level = ('xpath','//*[@id="divScreen"]/li[3]/a[5]')
    Level_path = ('xpath','/html/body/div[8]/div[1]/div/span[3]/a')
    Isellcar = ('xpath','/html/body/div[8]/div[2]/div[1]/a')
    sell_img = ('xpath','/html/body/div[7]/div[1]/div[1]/div/div/h3')
    Isellcarbutton = ('xpath', '/html/body/div[8]/div[2]/div[1]/a')
    pinggu_button = ('xpath', '/html/body/div[8]/div[2]/div[2]/a[2]')
    pinggu_img = ('xpath', '/html/body/div[7]/div[4]/div/div[1]')
    qgg = ('xpath', '//*[@id="bzcWrap"]/div/div[1]/a')
    qgg_tag = ('xpath', '//*[@id="container_base"]/ul/li[1]/div[2]/div[2]/em')
    Qgg_img = ('xpath', '//*[@id="tc_mendian_data"]/li[1]/div[2]/a')
    car_img = ('xpath', '//*[@id="taoche-details-pic"]/div[1]/div[2]')
    car_name = ('xpath', '//*[@id="tc_mendian_data"]/li[1]/div[3]/a')
    qgg_see = ('xpath', '//*[@id="bzcWrap"]/div/div[1]/a')
    new_car = ('xpath', '/html/body/div[9]/div[2]/div/div[2]/div[1]/a')
    new_img = ('xpath', '/html/body/section[2]/div[2]/ul/li[1]/a')
    calculater = ('xpath', '/html/body/div[9]/div[2]/div/div[2]/div[2]/div[1]/div[1]/a')
    calculater_button = ('xpath', '//*[@id="root"]/div/ul/li/a')
    fenqi_buy = ('xpath', '/html/body/div[9]/div[2]/div/div[2]/div[2]/div[1]/div[2]/a')
    fenqi_img = ('xpath', '/html/body/div[8]/section[1]/dl/dt/h3')
    online_buy = ('xpath', '/html/body/div[9]/div[2]/div/div[2]/div[2]/div[2]/a')
    online_name = ('xpath', '//*[@id="app"]/article/div[1]/div/div[2]/div/div[1]/div/span[1]')
    taoche_new = ('xpath', '/html/body/div[9]/div[2]/div/div[2]/div[2]/div[3]/div[1]/a')
    tiyandian = ('xpath', '/html/body/div[9]/div[2]/div/div[2]/div[2]/div[3]/div[2]/a')
    tiyandian_name = ('xpath', '//*[@id="app"]/div/section/div[2]/div[1]/div[1]/ul/ul/li[1]/a/h6')
    news_see = ('xpath', '/html/body/div[9]/div[5]/div/div[1]/a')
    news_title = ('xpath', '/html/body/div[7]/div[2]/div[1]')
    fist_img = ('xpath', '//*[@id="focus2"]/ul[1]/li[2]/a')
    see_button = ('xpath', '/html/body/div[9]/div[6]/div/a')
    show_title = ('xpath', '/html/body/div[7]/nav/a[2]')
    show_button = ('xpath', '/html/body/div[9]/div[6]/ul/li[1]/div[1]/a')
    about_button = ('xpath', '/html/body/div[10]/div/div[1]/ul/li[1]/a')
    about_title = ('xpath', '//*[@id="form1"]/div[3]/div/div[1]/div')
    contact_button = ('xpath', '/html/body/div[10]/div/div[1]/ul/li[2]/a')
    zhiye_button = ('xpath', '/html/body/div[10]/div/div[1]/ul/li[2]/a')
    zhiye_logo = ('xpath', '/html/body/div/div[1]/div/div[1]/img')
    license_url = ('xpath', '/html/body/div[10]/div/div[1]/ul/li[4]/a')
    ICP_url = ('xpath', '/html/body/div[10]/div/div[1]/ul/li[5]/a')
    TV_url = ('xpath', '/html/body/div[10]/div/div[1]/ul/li[6]/a')
    hot_shanghai = ('xpath', '/html/body/div[11]/div[1]/a[2]')
    hot_brand = ('xpath', '/html/body/div[11]/div[2]/a[1]')
    hot_series = ('xpath', '/html/body/div[11]/div[3]/a[1]')
    hot_car = ('xpath', '/html/body/div[11]/div[4]/a[1]')
    car_ask = ('xpath', '/html/body/div[11]/div[5]/a[1]')
    car_news = ('xpath', '/html/body/div[11]/div[5]/a[2]')
    car_vehicle = ('xpath', '/html/body/div[11]/div[5]/a[3]')
    find_car = ('xpath', '//*[@id="footer_sitemap"]/dl/dd/a[1]')
    xpath_all = ('xpath', '//a')
    first_car = ('xpath', '//*[@id="container_base"]/ul/li[1]/div[2]/a')








class HomePageLocator:
    # 焦点图
    FOCUS_PIC_IMG = ('xpath', '//*[@id="index_focus_pic"]/li/ins/img')
    FOCUS_PIC_JUMP = ('xpath', '//*[@id="index_focus_pic"]/li/ins/div[1]')

    # 我要买车
    # BUY_CAR = ('class', 'newhome-buyCar')
    BUY_CAR_TITLE = ('xpath', '//*[@class="newhome-buyCar"]/div/a')
    BUY_CAR_COLUMN = ('id', 'divScreen')
    BUY_CAR_BRAND = ('xpath', '//*[@id="divScreen"]/li[1]')
    BUY_CAR_PRICE = ('xpath', '//*[@id="divScreen"]/li[2]')
    BUY_CAR_LEVEL = ('xpath', '//*[@id="divScreen"]/li[3]')
    BUY_CAR_COLLECT =('xpath','//*[@id="addCollect"]')
    BUY_CAR_COLLECTED =('xpath','//*[@id="attentionA"]')
    BUY_CAR_COLLECTED_text =('xpath','//*[@id="attentionUl"]/li/h6/a')
    #BUY_CAR_COLLECTED_text1 = ('xpath', '//*[@id="attentionUl"]')
    Vehicle_name = ('xpath','/html/body/div[8]/div[1]/div[2]/div[1]/h1')



    # 我要卖车
    SELL_CAR_TITLE = ('xpath', '//*[@class="newhome-SellCar"]/div[1]/a')
    SELL_CAR_PHONE = ('id', '_phone')
    SELL_CAR_SUBMIT = ('xpath', '//*[@class="newhome-SellCar"]/div[2]/a[1]')
    SELL_CAR_PINGU = ('xpath', '//*[@class="newhome-SellCar"]/div[2]/a[2]')
    SELL_CAR_input = ('id','span_selectcarname')
    #SELL_CAR_BRAND = ('xpath','//*[@id="divCarType_letters_A"]')
    SELL_CAR_BRAND1 = ('id','divCarType_letters_A')
    AUDI_BRAND = ('xpath','//*[@id="divCarType_letters_A"]/p[1]/a')
    AUDI100_SER = ('xpath','//*[@id="divCarType_serial_list"]/div[1]/p[4]/a')
    #VEHICLE_SEL = ('text','1.8L')
    VEHICLE_SEL =('xpath','//*[@id="divCarType_cartype_list"]/div[1]/h4')
    SERIAL_DIR_ID = ('id','divCarType_cartype_list')
    license_plate =('xpath','//*[@id="span_oldcartime"]')
    license_plate_year = ('xpath','//*[@id="div_selectcartime"]/div[2]/div[1]/div/p[2]/a')
    license_plate_mounth = ('xpath','//*[@id="div_selectcartime"]/div[2]/div[2]/p[1]/a')
    #mileage =('xpath','//*[@id="txtMil"]')
    mileage =('id','txtMil')
    res_vehicle =('xpath','/html/body/div[8]/div[1]')
    telephone_input = ('xpath','//*[@id="txtPhone"]')
    evaluate_sell = ('xpath','//*[@id="evaluate_sell"]')
    price1 = ('xpath','//*[@id="condition"]/li[1]/a/i')
    price2 = ('id','ct_price')
    price3 = ('xpath','//*[@id="condition_A"]/a/i')




    # 楼层
    FLOORS = ('class', 'newhome-titleOne')



class BuyCarLocator:
    # 面包屑
    NAV_STATUS = ('class', 'Nav_Status')

    # 已选择条件
    FILTER_SELETED = ('class', 'Nav_selected')

    SUBMENU_TAB_ZY = ('id', 'tag_yjk')
    SUBMENU_TAB_FZY = ('xpath', '//*[@id="containerId"]/div[1]/div[3]/div[1]/ul[1]/li[1]')
    COMMON_TOOLS = ('xpath', '//*[@id="containerId"]/div[2]/div[1]/div[2]/ul')
    HOT_SERIAL = ('xpath', '//*[@id="hotSeoCarBrand"]')
    HOT_SERIAL_NAME = ('xpath', '//*[@id="div_hot_car"]/div[1]')
    HOT_BRAND_NAME = ('xpath', '//*[@id="div_hot_car"]/div[3]/ul')
    CAR_LIST_INFO = ('xpath', '//*[@id="container_base"]/ul/li[1]/div[1]/div')
    CAR_DETAIL_INFO = ('xpath', '/html/body/div[7]/div/a[6]')

    SEARCH_KEY_WORD = ('xpath', '//*[@id="tc_search_txtErshouche"]')
    SEARCH_ACTION = ('xpath', '//*[@id="tc_search_btnErshouche"]')
    SEARCH_RESULT = ('xpath', '//*[@id="containerId"]/div[1]/div[1]/ul/li[1]/a')
    SEARCH_HOT_BRAND_LIST = ('xpath', '//*[@id="divList"]')
    DEALER_INFO = ('xpath', '/html/body/div[8]/div[6]/div/div[2]/p[3]/a[2]')
    CITY_INFO = ('xpath', '/html/body/div[7]/div/a[2]')


class NewsLocator:
    NAV_NEWS = ('xpath', '//*[@id="ul_menu"]/li[5]')

#首页搜索框元素
class Search:
    Search_Box = ('xpath','//*[@id="tc_search_txtErshouche"]')
    Search_Button = ('xpath','//*[@id = "tc_search_btnErshouche"]')
    Dropdown_Box = ('xpath','//*[@id="divList"]/ul')
    hotRecordList = ('class','hotRecordList')
    Search_Reault =('xpath','//*[@id="divList"]/ul/li[1]/a/i')
    Result_aodi = ('xpath','//*[@id="containerId"]/div[1]/div[1]/ul/li[1]/a')
    Result_fengtian = ('xpath','//*[ @ id = "containerId"]/div[1]/div[1]/ul/i[1]/a')
    Search_Reault_new =('class','Nav_selected')
    SEARCH_TEXT = ('xpath','//*[@id="tc_search_txtErshouche"]')
    SEARCH_DROP_LIST_ID = ('id','divList')
    SEARCH_BRAND_NAME = ('xpath','//*[@id="containerId"]/div[1]/div[1]/ul/li[2]/a')

#买车列表筛选元素
class BuyCarTag:
    # 选择品牌的字母
    BUY_CAR_BRAND_CODE = ('xpath','//*[@id="brandMoreDiv"]/ul[1]')
    BUY_CAR_BRAND_CODE_LIST =('xpath','brandMoreDiv')
    # 获取字母A下面的品牌
    BUY_CAR_BRAND_CODE_A = ('id','brandlist_A')
    # 车系品牌列表
    CX_LIST = ('id', 'hotSerialId')
    # 筛选结果tag
    Submenu_tab = ("xpath", '//*[@ id = "containerId"]//li[1]/h1/a)')
    #列表页用户展示
    chexing_choose = ('xpath','//*[ @ id = "containerId"]/div[1]/div[1]')
    #页面实际展示品牌
    Result_brand_list = ('xpath', '//*[@id="containerId"]/div[1]/div[1]/ul/li[1]/a')
    #页面实际展示车系
    Result_CX_list = ('xpath', '//*[@id="containerId"]/div[1]/div[1]/ul/li[2]/a')
    #列表第一个tag回显的品牌
    show_list_tag_one = ('xpath', '//*[@id="containerId"]/div[1]/div[4]/div[1]/ul[1]/li[1]/h1/a')
    #列表页第一个车源的车型名称
    show_carOne_name = ('xpath', '//*[@id="container_base"]/ul/li[1]/div[1]/div/a')
    show_carlist = ('id','container_base')
    #列表页面包屑
    show_carlist_top = ('xpath', '/html/body/div[8]/div[1]')
    #获取列表自定义元素
    customer_price_btn = ('id',"priceword")
    customer_price_box = ('id',"priceDiv")
    price_inputMin_box = ('id',"price_min")
    price_inputMax_box = ('id',"price_max")
    price_Determine_btn = ('id',"aprice_ok")
    price_TH = ('class' ,'Total brand_col')
#    price_GD = ('xpath' ,'//*[@id="container_base"]/ul/li[1]/div[2]/div[1]/i[2]')
    shs = '//*[@id="container_base"]/ul/li[1]/div[2]/div[1]/i[2])'

    CAR_FIRST_CLICLK = ('xpath','//*[@id="container_base"]/ul/li[1]/div[2]/a')




