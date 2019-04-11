#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from page_location import memberCenterLocation as memLocation
import basePage
from basePage import login,GetPageSize,swipe_up
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
        old_tag = memLocation.old_tag % tag

        login(self, business, username, password)
        time.sleep(5)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
        time.sleep(2)
        # 进入会员中心
        self.click_element(memLocation.menu_info)
        time.sleep(2)
        if self.find_element(memLocation.iterm):
            self.click_element(memLocation.text_confirm)
        # 输入会员手机号码
        for num in telphone:
            self.driver.press_keycode(basePage.keycode[num])
        # 搜索会员
        self.click_element(memLocation.search_product_btn)
        time.sleep(5)
        if self.find_element(memLocation.iterm):
            self.click_element(memLocation.text_confirm)
        self.click_element(memLocation.radio_history)
        time.sleep(2)
        self.click_element(memLocation.coupon_layout)
        time.sleep(2)
        if self.find_element(memLocation.iterm):
            self.click_element(memLocation.text_confirm)
        self.click_element(memLocation.radio_pic)
        self.click_element(memLocation.addTagBtn)
        self.input_element(memLocation.custom_targs, tag)
        self.click_element(memLocation.add_targs_button)
        time.sleep(2)
        self.click_element(memLocation.confirm_button)
        time.sleep(2)
        # 验证标签是否添加成功
        if self.find_element(memLocation.old_tag):
            print '会员标签添加成功'
        else:
            raise Exception('会员标签添加失败')
        self.click_element(memLocation.member_back)
        self.click_element(basePage.menu_btn_layout)
        sx = 0.1
        sy = 0.25
        ex = 0.1
        ey = 0.75
        swipe_up(self, GetPageSize(self), sx, sy, ex, ey)
        self.click_element(basePage.logout)
        self.click_element(basePage.text_confirm)

    def member_register(self, business, username, password, tag):
        '''
        注册会员，添加新会员标签
        '''

        login(self,business, username, password)
        time.sleep(5)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
        time.sleep(2)
        # 进入会员中心
        self.click_element(memLocation.menu_info)
        time.sleep(2)
        if self.find_element(memLocation.iterm):
            self.click_element(memLocation.text_confirm)
        new_member = self.createPhone()
        for new_num in new_member:
            self.driver.press_keycode(basePage.keycode[new_num])
        self.click_element(memLocation.add_member_txt)
        time.sleep(2)
        if self.find_element(memLocation.hint_text):
            self.click_element(memLocation.text_confirm)
        time.sleep(5)
        new_name = self.memberName().decode('utf-8')
        self.input_element(memLocation.register_name, new_name)
        self.click_element(random.choice(memLocation.sex))
        self.click_element(memLocation.register_save)
        time.sleep(2)
        self.tag_info = self.tag_info % new_member
        if self.find_element(self.tag_info):
            self.click_element(memLocation.text_confirm)
        time.sleep(5)
        if self.find_element(memLocation.iterm):
            self.click_element(memLocation.text_confirm)
        self.click_element(memLocation.radio_pic)
        self.click_element(memLocation.addTagBtn)
        self.input_element(memLocation.custom_targs, tag)
        self.click_element(memLocation.add_targs_button)
        time.sleep(2)
        self.click_element(memLocation.confirm_button)
        time.sleep(2)
        # 验证标签是否添加成功
        if self.find_element(memLocation.old_tag):
            print '会员标签添加成功'
        else:
            raise Exception('会员标签添加失败')
        time.sleep(2)
        # 使用新注册的会员进行下单
        self.click_element(memLocation.sale_btn)
        try:
            self.find_element(memLocation.member_name.text == new_name)
            print '跳转到购物车页面成功带上会员'
        except:
            raise Exception('异常')
        self.click_element(basePage.menu_btn_layout)
        sx = 0.1
        sy = 0.25
        ex = 0.1
        ey = 0.75
        swipe_up(self, GetPageSize(self), sx, sy, ex, ey)
        self.click_element(basePage.logout)
        self.click_element(basePage.text_confirm)
