#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from ios_page_location import memberCenterLocation as memLocation
from ios_page_location import basePage
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class MemberCenter(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    # 会员查询
    def member_query(self, business, username, password, telphone):
        '''
        搜索会员，会员画像，会员资料，历史订单，优惠券
        '''
        basePage.login(self, business, username, password)
        time.sleep(6)
        try:
            # 点击菜单
            self.click_acc(basePage.menu)
            time.sleep(2)
            # 进入会员中心
            self.click_element(memLocation.menu_info)
            time.sleep(2)
            # 输入会员手机号码
            for num in telphone:
                self.click_acc('%s'%num)
            # 搜索会员
            self.click_acc(memLocation.search_member)
            time.sleep(5)
            # self.click_element(memLocation.radio_history)
            # time.sleep(2)
            # self.click_acc(memLocation.coupon_layout)
            # time.sleep(2)
            # self.click_element(memLocation.radio_pic)
            # time.sleep(2)

            self.click_acc(memLocation.addTagBtn)
            time.sleep(1)
            self.click_acc(memLocation.memberTagSettingIcon)
            time.sleep(1)
            self.click_acc(memLocation.clear_all)
            time.sleep(1)
            self.click_element(memLocation.tags)
            time.sleep(1)
            self.click_acc(memLocation.confirm)
            time.sleep(2)
            self.click_element(memLocation.message)
            time.sleep(2)

            # contexts = self.driver.contexts
            # # print contexts
            # time.sleep(2)
            # print self.driver.page_source
            self.click_acc(memLocation.back_btn)
            time.sleep(1)
            self.click_acc(basePage.menu)
        except Exception as e:
            raise Exception('会员中心出现异常%s'%e)

    # # 会员注册
    def member_register(self, business, username, password):
        '''
        注册会员，添加新会员标签
        '''

        basePage.login(self,business, username, password)
        time.sleep(6)
        try:
            # 点击菜单
            self.click_acc(basePage.menu)
            time.sleep(2)
            # 进入会员中心
            self.click_element(memLocation.menu_info)
            time.sleep(2)
            new_member = basePage.createPhone()
            for num in new_member:
                self.click_acc('%s' % num)
            self.click_acc(memLocation.register_member)
            time.sleep(5)
            new_name = basePage.member_name().decode('utf-8')
            self.input_element(memLocation.member_name, new_name)
            time.sleep(1)
            print self.driver.page_source
            self.click_acc(basePage.disappear_keyboard)
            time.sleep(1)
            self.input_element(memLocation.mail,basePage.create_mail())
            time.sleep(1)
            self.click_acc(basePage.disappear_keyboard)
            time.sleep(1)
            self.click_acc(memLocation.register_confirm)
            time.sleep(3)
            # 使用新注册的会员进行下单
            # self.click_acc(memLocation.member_sale_btn)
            time.sleep(1)
            self.click_acc(memLocation.back_btn)
        except Exception as e:
            raise Exception('会员中心添加标签出现异常%s'%e)
