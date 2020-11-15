class InitLocator:

    #手机权限确认
    MOBILE_LIMIT = ("xpath", "//*[@text='始终允许']")
    #app评价提示
    GRADE_REJECT = ("id", "com.umetrip.android.msky.app:id/tv_reject")
    #appMenu
    MENU_BAR = ("id", "com.umetrip.android.msky.app:id/tv_text")


class MineLocator:
    # 登录
    HEAD_LOGIN = ("xpath", "//*[@text='点击登录']")
    TEST123 = ("id", "com.umetrip.android.msky.app:id/regist_name_edit")
    TEST234 = ("id", "com.umetrip.android.msky.app:id/regist_name_edit")
    TEST1111 = ("id", "com.umetrip.android.msky.app:id/regist_pass_edit")


class HomeLoctor:
    SEARCH_MORE = ("id","com.ucar.app:id/home ._filter_more")
    SEARCH_CLICK = ("id","com.ucar.app:id/tv_search")
    SEARCH_KEY = ("id", "com.ucar.app:id/actv_search")

    BRAND_KEY = ('id','com.ucar.app:id/home_page_brand_text')
    CAR_LIST_SCREEN_ID = ('id','com.ucar.app:id/v_has_screen')
    CAR_INFO_ID = ('id','com.ucar.app:id/view_bottom_line')
    CAR_INFO_IDS = ('id','com.ucar.app:id/tv_car_name')
    DETAIL_CAR_NAME = ('id','com.ucar.app:id/tv_car_name')
    QGG_FLOOR_ID = ('id','com.ucar.app:id/tv_car_store_name')

    # 五个吸底tab id
    SHOUYE_ID = ('id','com.ucar.app:id/rlTabHome')

    # 新车楼层
    XINCHETUIJIAN_ID = ('id','com.ucar.app:id/new_car_left_layout')
    XINCHEH5_TEXT_ID = ('id','com.ucar.app:id/base_tv_center')
    XINCHEH5_BACK_ID = ('id','com.ucar.app:id/base_iv_left')
    KAIZOUBA_ID = ('id','com.ucar.app:id/new_car_top_layout')
    FENQIGOUCHE_ID = ('id','com.ucar.app:id/new_car_bottom_layout')

    #首页推荐区楼层
    JINRISHANGXIN_IDS = ('id','com.ucar.app:id/ll_big_left')
    JINRISHANGXIN_TEXT_IDS = ('id','com.ucar.app:id/tv_big_left_title')
    JINRISHANGXIN_SUBTITLE_IDS = ('id','com.ucar.app:id/tv_big_left_subtitle')
    ZHUNXINCHE_IDS = ('id','com.ucar.app:id/ll_small_left')
class  BuyCarLocator:
    TAB = ("id", "com.ucar.app: id / txtTabBuy")#买车TAB
    SEARCH_INPUT=("id","com.ucar.app:id/ll_search")#搜索输入框
    CITY=("id","com.ucar.app:id/base_tv_left")#城市选择
    # 沈阳
    SY=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.GridView/android.widget.TextView[7]")
    #关闭城市选择框
    CITY_CLOSE=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")
   #保真车
    BZC=("ID",)
    #淘车直营
    TCZY = ("ID","com.ucar.app:id/xlistview_header_progressbar")
    #全国购
    QGG=("ID","com.ucar.app:id/xlistview_header_hint_textview")
    #排序
    PX=("id","com.ucar.app:id/btnSort")
    #价格最低
    JGZD=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
    #价格筛选框“
    JG=("id","com.ucar.app:id/btnPrice")
    #价格100万以上
    JG1=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[11]/android.widget.TextView")
    #价格最低车源价格
    JDFIRST=("xpath","self.driver.find_element(BuyCarLocator.JG1).click()")



class  SellCarLocator:
    TAB=("id","com.ucar.app:id/imgTabSell")#卖车TAB
    TITLE=("id","com.ucar.app:id/base_tv_center")#卖车页面标题


