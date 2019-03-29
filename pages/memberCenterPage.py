#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from selenium.webdriver.common.by import By
import basePage
import time
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class MemberCenter(BaseFunction):
    def __init__(self,driver):
        BaseFunction.__init__(self,driver)

    def login(self,business,username,password):
        # 输入商户号
        self.input_element(basePage.edit_business,business)
        # 输入用户名
        self.input_element(basePage.edit_username, username)
        # 定位username，防止自动提示导致回删数据
        self.click_element(basePage.edit_username)
        # 输入密码
        self.input_element(basePage.edit_password, password)
        # 点击登录
        self.click_element(basePage.text_login)
        # 验证是否登录成功
        try:
            self.find_element(basePage.shop_title)
            print '登录成功'
        except:
            self.fail('登录失败')

    # 注册会员
    def createPhone(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

    # 随机生成会员name
    def memberName(self):
        a1 = ['张', '金', '李', '王', '赵']
        a2 = ['玉', '明', '龙', '芳', '军', '玲']
        a3 = ['', '立', '玲', '', '国', '']
        return random.choice(a1) + random.choice(a2) + random.choice(a3)


    def member_query(self,business,username,password,telphone,tag):
        '''
        搜索会员，会员画像，会员资料，历史订单，优惠券
        '''
        # 会员中心button
        self.menu_info = (By.XPATH, "//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[3]")
        # 未绑定二维码会弹出提示信息
        self.iterm = (By.XPATH, "//android.widget.TextView[contains(@text,'收银终端[POS-漂亮]未绑定二维码')]")
        # 查看该会员是否已经存在要添加的标签
        self.old_tag = (By.XPATH, "//android.widget.TextView[contains(@text,%s)]"%tag)
        # 确认提示操作
        self.text_confirm = (By.ID, 'com.nexttao.shopforce.test:id/text_confirm')
        # 搜索button
        self.search_product_btn = (By.ID, 'com.nexttao.shopforce.test:id/search_product_btn')
        # 添加标签button
        self.addTagBtn = (By.ID, 'com.nexttao.shopforce.test:id/addTagBtn')
        # 自定义标签输入框
        self.custom_targs = (By.ID, 'com.nexttao.shopforce.test:id/custom_targs')
        # 确认添加标签button
        self.add_targs_button = (By.ID, 'com.nexttao.shopforce.test:id/add_targs_button')
        # 确定button
        self.confirm_button = (By.ID, 'com.nexttao.shopforce.test:id/confirm_button')
        # 验证标签是否添加成功
        self.tags_text = (By.XPATH, "//android.widget.TextView[contains(@text,tag)]")
        # 会员画像
        self.radio_pic = (By.ID, 'com.nexttao.shopforce.test:id/radio_pic')
        # 历史订单
        self.radio_history = (By.ID, 'com.nexttao.shopforce.test:id/radio_history')
        # 优惠券
        self.coupon_layout = (By.ID, 'com.nexttao.shopforce.test:id/coupon_layout')
        # 返回button
        self.member_back = (By.ID, 'com.nexttao.shopforce.test:id/member_back')

        self.login(business,username,password)
        time.sleep(5)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
        time.sleep(2)
        # 进入会员中心
        self.click_element(self.menu_info)
        time.sleep(2)
        if self.find_element(self.iterm):
            self.click_element(self.text_confirm)
        # 输入会员手机号码
        for num in telphone:
            self.driver.press_keycode(basePage.keycode[num])
        # 搜索会员
        self.click_element(self.search_product_btn)
        time.sleep(5)
        if self.find_element(self.iterm):
            self.click_element(self.text_confirm)
        self.click_element(self.radio_history)
        time.sleep(2)
        self.click_element(self.coupon_layout)
        time.sleep(2)
        if self.find_element(self.iterm):
            self.click_element(self.text_confirm)
        self.click_element(self.radio_pic)
        self.click_element(self.addTagBtn)
        self.input_element(self.custom_targs, tag)
        self.click_element(self.add_targs_button)
        time.sleep(2)
        self.click_element(self.confirm_button)
        time.sleep(2)
        # 验证标签是否添加成功
        if self.find_element(self.old_tag):
            print '会员标签添加成功'
        else:
            print '会员标签添加失败'
        self.click_element(self.member_back)
        time.sleep(2)

    def member_register(self,business,username,password,tag):
        '''
        注册会员，添加新会员标签
        '''
        # 会员中心button
        self.menu_info = (By.XPATH, "//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[3]")
        # 未绑定二维码会弹出提示信息
        self.iterm = (By.XPATH, "//android.widget.TextView[contains(@text,'收银终端[POS-漂亮]未绑定二维码')]")
        # 确认提示操作
        self.text_confirm = (By.ID, 'com.nexttao.shopforce.test:id/text_confirm')
        # 添加标签button
        self.addTagBtn = (By.ID, 'com.nexttao.shopforce.test:id/addTagBtn')
        # 自定义标签输入框
        self.custom_targs = (By.ID, 'com.nexttao.shopforce.test:id/custom_targs')
        # 确认添加标签button
        self.add_targs_button = (By.ID, 'com.nexttao.shopforce.test:id/add_targs_button')
        # 确定button
        self.confirm_button = (By.ID, 'com.nexttao.shopforce.test:id/confirm_button')
        # 验证标签是否添加成功
        self.tags_text = (By.XPATH, "//android.widget.TextView[contains(@text,tag)]")
        # 注册会员
        self.add_member_txt = (By.ID, 'com.nexttao.shopforce.test:id/add_member_txt')
        # 提示信息
        self.hint_text = (By.ID, 'com.nexttao.shopforce.test:id/hint_text')
        # 会员姓名
        self.register_name = (By.ID, 'com.nexttao.shopforce.test:id/register_name')
        # 会员性别
        self.sex = [(By.ID, 'com.nexttao.shopforce.test:id/checkman'),
                    (By.ID, 'com.nexttao.shopforce.test:id/checkwomen')]
        # 注册button
        self.register_save = (By.ID, 'com.nexttao.shopforce.test:id/register_save')
        # 确认注册
        self.tag_info = (By.XPATH, "//android.widget.TextView[contains(@text,'%s')]")
        # 会员画像
        self.radio_pic = (By.ID, 'com.nexttao.shopforce.test:id/radio_pic')
        # 历史订单
        self.radio_history = (By.ID, 'com.nexttao.shopforce.test:id/radio_history')
        # 优惠券
        self.coupon_layout = (By.ID, 'com.nexttao.shopforce.test:id/coupon_layout')
        # 改会员改单button
        self.sale_btn = (By.ID, 'com.nexttao.shopforce.test:id/sale_btn')
        # 验证是否将会员信息带到购物车页面
        self.member_name = (By.ID, 'com.nexttao.shopforce.test:id/member_name')

        self.login(business, username, password)
        time.sleep(5)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
        time.sleep(2)
        # 进入会员中心
        self.click_element(self.menu_info)
        time.sleep(2)
        if self.find_element(self.iterm):
            self.click_element(self.text_confirm)
        new_member = self.createPhone()
        for new_num in new_member:
            self.driver.press_keycode(basePage.keycode[new_num])
        self.click_element(self.add_member_txt)
        time.sleep(2)
        if self.find_element(self.hint_text):
            self.click_element(self.text_confirm)
        time.sleep(5)
        new_name = self.memberName().decode('utf-8')
        self.input_element(self.register_name, new_name)
        self.click_element(random.choice(self.sex))
        self.click_element(self.register_save)
        time.sleep(2)
        self.tag_info = self.tag_info % new_member
        if self.find_element(self.tag_info):
            self.click_element(self.text_confirm)
        time.sleep(5)
        if self.find_element(self.iterm):
            self.click_element(self.text_confirm)
        self.click_element(self.radio_pic)
        self.click_element(self.addTagBtn)
        self.input_element(self.custom_targs, tag)
        self.click_element(self.add_targs_button)
        time.sleep(2)
        self.click_element(self.confirm_button)
        time.sleep(2)
        # 验证标签是否添加成功
        if self.find_element(self.old_tag):
            print '会员标签添加成功'
        else:
            print '会员标签添加失败'
        time.sleep(2)
        # 使用新注册的会员进行下单
        self.click_element(self.sale_btn)
        try:
            self.find_element(self.member_name).text == new_name
            raise '跳转到购物车页面成功带上会员'
        except:
            raise '异常'





