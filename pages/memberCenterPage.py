#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
import memberCenterLocation as mcLocation
import basePage
from basePage import login
import time
import random
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class MemberCenter(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    # 注册会员
    def createPhone(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

    # 随机生成会员name
    def memberName(self):
        a1 = ['张', '金', '李', '王', '赵']
        a2 = ['玉', '明', '龙', '芳', '军', '玲']
        a3 = ['', '立', '玲', '国']
        return random.choice(a1) + random.choice(a2) + random.choice(a3)

    def member_query(self, business, username, password, telphone, tag):
        '''
        搜索会员，会员画像，会员资料，历史订单，优惠券
        '''
        old_tag = mcLocation.old_tag % tag

        login(self, business, username, password)
        time.sleep(5)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
        time.sleep(2)
        # 进入会员中心
        self.click_element(mcLocation.menu_info)
        time.sleep(2)
        if self.find_element(mcLocation.iterm):
            self.click_element(mcLocation.text_confirm)
        # 输入会员手机号码
        for num in telphone:
            self.driver.press_keycode(basePage.keycode[num])
        # 搜索会员
        self.click_element(mcLocation.search_product_btn)
        time.sleep(5)
        if self.find_element(mcLocation.iterm):
            self.click_element(mcLocation.text_confirm)
        self.click_element(mcLocation.radio_history)
        time.sleep(2)
        self.click_element(mcLocation.coupon_layout)
        time.sleep(2)
        if self.find_element(mcLocation.iterm):
            self.click_element(mcLocation.text_confirm)
        self.click_element(mcLocation.radio_pic)
        self.click_element(mcLocation.addTagBtn)
        self.input_element(mcLocation.custom_targs, tag)
        self.click_element(mcLocation.add_targs_button)
        time.sleep(2)
        self.click_element(mcLocation.confirm_button)
        time.sleep(2)
        # 验证标签是否添加成功
        if self.find_element(mcLocation.old_tag):
            print '会员标签添加成功'
        else:
            raise Exception('会员标签添加失败')
        self.click_element(mcLocation.member_back)
        time.sleep(2)

    def member_register(self, business, username, password, tag):
        '''
        注册会员，添加新会员标签
        '''

        self.login(business, username, password)
        time.sleep(5)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
        time.sleep(2)
        # 进入会员中心
        self.click_element(mcLocation.menu_info)
        time.sleep(2)
        if self.find_element(mcLocation.iterm):
            self.click_element(mcLocation.text_confirm)
        new_member = self.createPhone()
        for new_num in new_member:
            self.driver.press_keycode(basePage.keycode[new_num])
        self.click_element(mcLocation.add_member_txt)
        time.sleep(2)
        if self.find_element(mcLocation.hint_text):
            self.click_element(mcLocation.text_confirm)
        time.sleep(5)
        new_name = self.memberName().decode('utf-8')
        self.input_element(mcLocation.register_name, new_name)
        self.click_element(random.choice(mcLocation.sex))
        self.click_element(mcLocation.register_save)
        time.sleep(2)
        self.tag_info = self.tag_info % new_member
        if self.find_element(self.tag_info):
            self.click_element(mcLocation.text_confirm)
        time.sleep(5)
        if self.find_element(mcLocation.iterm):
            self.click_element(mcLocation.text_confirm)
        self.click_element(mcLocation.radio_pic)
        self.click_element(mcLocation.addTagBtn)
        self.input_element(mcLocation.custom_targs, tag)
        self.click_element(mcLocation.add_targs_button)
        time.sleep(2)
        self.click_element(mcLocation.confirm_button)
        time.sleep(2)
        # 验证标签是否添加成功
        if self.find_element(mcLocation.old_tag):
            print '会员标签添加成功'
        else:
            raise Exception('会员标签添加失败')
        time.sleep(2)
        # 使用新注册的会员进行下单
        self.click_element(mcLocation.sale_btn)
        try:
            self.find_element(mcLocation.member_name.text == new_name)
            print '跳转到购物车页面成功带上会员'
        except:
            raise Exception('异常')
