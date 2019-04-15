#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
from base_appium_function.base_function import BaseFunction

'''
    keycode信息,key为实际要输入的数字，value表示key所对应的键盘值
'''
keycode = {
    '0': 7,
    '1': 8,
    '2': 9,
    '3': 10,
    '4': 11,
    '5': 12,
    '6': 13,
    '7': 14,
    '8': 15,
    '9': 16
}
# 登录页面相关的id
# 网络连接失败的提示
hint_text = (By.XPATH, "//android.widget.TextView[contains(@text,'网络连接失败,请检查网络连接')]")
# 定位商户号输入框
edit_business = (By.ID, 'com.nexttao.shopforce.test:id/edit_business')
# 定位用户名输入框
edit_username = (By.ID, 'com.nexttao.shopforce.test:id/edit_username')
# 定位密码输入框
edit_password = (By.ID, 'com.nexttao.shopforce.test:id/edit_password')
# 定位登录
text_login = (By.ID, 'com.nexttao.shopforce.test:id/text_login')
# 验证是否登录成功,拿到购物车title
shop_title = (By.ID, 'com.nexttao.shopforce.test:id/shopcar_title')
# 展开菜单button
menu_btn_layout = (By.ID, 'com.nexttao.shopforce.test:id/menu_btn_layout')
# 登出
logout = (By.XPATH, "//android.widget.TextView[contains(@text,'登出')]")
# 确认登出
text_confirm = (By.ID, 'com.nexttao.shopforce.test:id/text_confirm')
# 设置面板
settings = (By.XPATH, "//android.widget.TextView[contains(@text,'设置面板')]")
# 数据更新
update_data = (By.XPATH, "//android.widget.TextView[contains(@text,'数据更新')]")
# 清空缓存
system_cache_clear_tv = (By.ID, 'com.nexttao.shopforce.test:id/system_cache_clear_tv')
# 更新产品或促销进度条
update_text_info = (By.ID, 'com.nexttao.shopforce.test:id/update_text_info')
# 商品搜索
keypad_search_btn = (By.ID, 'com.nexttao.shopforce.test:id/keypad_search_btn')


# 商品排列组合
# python 实现N个数组的排列组合(笛卡尔积算法)
class Cartesian():
    # 初始化
    def __init__(self, datagroup):
        self.datagroup = datagroup
        # 二维数组从后往前下标值
        self.counterIndex = len(datagroup) - 1
        # 每次输出数组数值的下标值数组(初始化为0)
        self.counter = [0 for i in range(0, len(self.datagroup))]

    # 计算数组长度
    def countlength(self):
        i = 0
        length = 1
        while (i < len(self.datagroup)):
            length *= len(self.datagroup[i])
            i += 1
        return length

    # 递归处理输出下标
    def handle(self):
        # 定位输出下标数组开始从最后一位递增
        self.counter[self.counterIndex] += 1
        # 判断定位数组最后一位是否超过长度，超过长度，第一次最后一位已遍历结束
        if self.counter[self.counterIndex] >= len(self.datagroup[self.counterIndex]):
            # 重置末位下标
            self.counter[self.counterIndex] = 0
            # 标记counter中前一位
            self.counterIndex -= 1
            # 当标记位大于等于0，递归调用
            if self.counterIndex >= 0:
                self.handle()
                # 重置标记
                self.counterIndex = len(self.datagroup) - 1

    # 排列组合输出
    def assemble(self):
        length = self.countlength()
        i = 0
        ll = []
        while (i < length):
            attrlist = []
            j = 0
            while (j < len(self.datagroup)):
                attrlist.append((self.datagroup[j][self.counter[j]]))
                j += 1
            ll.append(attrlist)
            self.handle()
            i += 1
        return ll


def login(basefunction, business, username, password):
    # 如果启动程序时网络连接失败的处理方式
    ex =  basefunction.find_element(hint_text)
    if ex:
        raise Exception('网络连接失败,请检查网络连接')
    # 输入商户号
    basefunction.input_element(edit_business, business)
    # 输入用户名
    basefunction.input_element(edit_username, username)
    # 定位username，防止自动提示导致回删数据
    basefunction.click_element(edit_username)
    # 输入密码
    basefunction.input_element(edit_password, password)
    # 点击登录
    basefunction.click_element(text_login)
    # 验证是否登录成功
    try:
        basefunction.find_element(shop_title)
        print '登录成功'
    except:
        raise Exception('登录失败')


# 获取屏幕尺寸
def GetPageSize(self):
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']
    return (x, y)


# 页面滑动
def swipe_up(self, page_size,s_x,s_y,e_x,e_y):
    sx = page_size[0] * s_x
    sy = page_size[1] * s_y
    ex = page_size[0] * e_x
    ey = page_size[1] * e_y
    self.driver.swipe(sx, sy, ex, ey, '500')

