#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random
import time
import datetime

# ===================>>>>>>>登录页面<<<<<<<<===============================
app = '互道盈力Beta'
# 商户号
merchantID = (By.XPATH, '//XCUIElementTypeApplication[@name="%s"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[1]'%app)
# 用户名
username = (By.XPATH,'//XCUIElementTypeApplication[@name="%s"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[2]'%app)
# password
password = (By.XPATH,'//XCUIElementTypeSecureTextField[@value="请输入您的密码"]')
# 隐藏键盘
disappear_keyboard = '隐藏键盘'
# 登录
login_button = '登  录'
# source
keyboard_search = (By.XPATH,'//XCUIElementTypeButton[@name="搜索"])[1]')
# 升级提示，确定
update_confirm = '确定'
# 升级提示，取消
update_cancel = '取消'

# ===================>>>>>>>通用元素<<<<<<<<===============================
# 菜单
menu = 'menu+status ok'
# 数据罗盘button
dashboard_item_name = '数据罗盘'
# 查询报表
report_item_name = '查询报表'
# 畅销排行
best_selling = '畅销排行'

# ===================>>>>>>>高级搜索<<<<<<<<===============================

# 高级搜索
search_advanced = '高级筛选－未点亮'
# 单据、小票
receipts = {'sale_order':(By.XPATH,'//XCUIElementTypeTextField[@value="请输入销售订单号"]'),'tran_order':(By.XPATH,'//XCUIElementTypeTextField[@value="请输入销售订单号"]')}
# sku
sku = (By.XPATH,'//XCUIElementTypeTextField[@value="请输入SKU"]')
# 日期范围
start_date = (By.XPATH,'//XCUIElementTypeImage[@name="高级选项-日期icon"])[1]')
end_date = (By.XPATH,'//XCUIElementTypeImage[@name="高级选项-日期icon"])[2]')
# 会员
member_phone = (By.XPATH,'//XCUIElementTypeTextField[@value="请输入手机号/会员卡号"]')
# 扫描会员码
member_qr_code = '扫描会员码'
# 公众号查找
search_pub_add = '公众号查找'
# 默认值，导购
default_sale_man = '全部导购'
# 默认值，付款方式
default_pay_type = '全部付款方式'
# 默认值，单据状态
default_order_state = '全部状态'
# 取消
cancel = '取消'
# 搜索
search = '搜索'
# 重置
reset = '重置'



# ===================>>>>>>>登录<<<<<<<<===============================

def login(basefunction, business, text_username, text_password):
    time.sleep(3)
    basefunction.click_acc(update_cancel)
    time.sleep(1)
    # 输入商户号
    # basefunction.input_element(merchantID, business)
    # # 输入用户名
    # basefunction.input_element(username, text_username)
    # 输入密码
    basefunction.input_element(password, text_password)
    # 隐藏键盘
    basefunction.click_acc(disappear_keyboard)
    # 登录
    basefunction.click_acc(login_button)

# ===================>>>>>>>随机生成手机号<<<<<<<<===============================

def createPhone():
    prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
    return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))

# ===================>>>>>>>随机生成邮箱<<<<<<<<===============================

def create_mail():
    mail_num = '0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ'
    random_num = "".join(random.choice(mail_num) for i in range(11))
    return random_num+'@163.com'

# ===================>>>>>>>随机生成姓名<<<<<<<<===============================

def member_name():
    a1 = ['张', '金', '李', '王', '赵']
    a2 = ['玉', '明', '龙', '芳', '军', '玲']
    a3 = ['', '立', '玲', '', '国', '']
    return random.choice(a1)+random.choice(a2)+random.choice(a3)

# ===================>>>>>>>获取屏幕尺寸<<<<<<<<===============================

def GetPageSize(self):
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']
    return (x, y)

def swipe_up(self, page_size, s_x, s_y, e_x, e_y):
    sx = page_size[0] * s_x
    sy = page_size[1] * s_y
    ex = page_size[0] * e_x
    ey = page_size[1] * e_y
    self.driver.swipe(sx, sy, ex, ey, '500')

# ===================>>>>>>><<<<<<<<===============================

def h5_swipe_up(self, s_x, s_y, e_x, e_y, time_out=2):
    contexts = self.driver.contexts
    self.switch_h5(contexts[0])
    time.sleep(time_out)
    page_size = GetPageSize(self)
    swipe_up(self, page_size, s_x, s_y, e_x, e_y)
    contexts = self.driver.contexts
    self.driver.switch_to.context(contexts[1])
    time.sleep(time_out)

# ===================>>>>>>><<<<<<<<===============================

def location_click(self, locals, click_time=500, time_out=2):
    contexts = self.driver.contexts
    self.switch_h5(contexts[0])
    time.sleep(time_out)
    page_size = GetPageSize(self)
    click_locals = [(page_size[0] * x, page_size[1] * y) for (x, y) in locals]
    self.driver.tap(click_locals, click_time)
    contexts = self.driver.contexts
    self.driver.switch_to.context(contexts[1])
    time.sleep(time_out)

# ===================>>>>>>>货架名称<<<<<<<<===============================
def get_rack_name():
    now = datetime.datetime.now()
    time_str = now.strftime('%y%m%d%H%M%S') + ("%02d" % (datetime.datetime.now().microsecond / 10000))
    random_str = "%06d%s%s%s%s" % (
    random.randint(0, 999999), chr(random.randint(65, 90)), chr(random.randint(97, 122)), chr(random.randint(97, 122)),
    chr(random.randint(65, 90)))
    rack_name = time_str + random_str
    return rack_name



# ===================>>>>>>>高级搜索，根据小票号<<<<<<<<===============================

def search_advanced_receipts(basefunction,business_no,receipts_type):
    basefunction.click_acc(search_advanced)
    time.sleep(2)
    print basefunction.driver.page_source
    basefunction.click_element(receipts[receipts_type])
    basefunction.input_element(receipts[receipts_type], business_no)
    basefunction.click_acc(disappear_keyboard)
    time.sleep(1)
    basefunction.click_acc(search)

# ===================>>>>>>>高级搜索，根据sku<<<<<<<<===============================

def search_advanced_sku(basefunction,sku_info):
    basefunction.click_acc(search_advanced)
    time.sleep(2)
    print basefunction.driver.page_source
    basefunction.click_element(sku)
    basefunction.input_element(sku, sku_info)
    basefunction.click_acc(disappear_keyboard)
    time.sleep(1)
    basefunction.click_acc(search)