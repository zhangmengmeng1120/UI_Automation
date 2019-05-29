#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from basePage import login, swipe_up, GetPageSize
import basePage
from android_page_location import deliveryReceiveLocation as deLocation
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class DeliveryReceive(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def delivery_confirm(self, business, username, password):
        '''
        签收待签收的单据
        :param business:
        :param username:
        :param password:
        :return:
        '''
        login(self, business, username, password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            time.sleep(2)
            if update_info == False: break
        try:
            # 点击菜单
            self.click_element(basePage.menu_btn_layout)
            # 向上滑到页面
            page_size = GetPageSize(self)
            sx = 0.1
            sy = 0.75
            ex = 0.1
            ey = 0.25
            swipe_up(self, page_size, sx, sy, ex, ey)
            # 点击门店入库
            self.click_element(deLocation.stock_in)
            # 点击配货收货
            self.click_element(deLocation.delivery_receive)
            time.sleep(2)
            self.click_element(deLocation.details_text)
            contexts = self.driver.contexts
            self.switch_h5(contexts[1])
            time.sleep(4)
            self.click_element(deLocation.icon_edit)
            self.click_element(deLocation.icon_delete)
            self.click_element(deLocation.num_key)
            self.click_element(deLocation.key_confirm)
            self.click_element(deLocation.btn_save)
            self.click_element(deLocation.back_btn)
            time.sleep(4)
            contexts = self.driver.contexts
            self.switch_h5(contexts[0])
            time.sleep(2)
            self.click_element(deLocation.take_receive)
            el = self.find_element(deLocation.transfer_diff_wizard)
            if el:
                self.click_element(deLocation.diff_confirm_button)
                time.sleep(3)
            self.click_element(deLocation.text_confirm_button)
            time.sleep(1)
            self.click_element(basePage.menu_btn_layout)
            page_size = GetPageSize(self)
            swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
            self.click_element(basePage.logout)
            self.click_element(basePage.text_confirm)
        except:
            raise Exception('签收配货收货单出现异常')


    def delivery_by_orderno(self, business, username, password, transferin_order, sku):
        '''
        调拨入库单高级搜索,根据调拨单号进行模糊搜索
        :return:
        '''
        # 登录
        login(self, business, username, password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            print update_info
            time.sleep(2)
            if update_info == False: break
        try:
            # 点击菜单
            self.click_element(basePage.menu_btn_layout)
            # 向上滑到页面
            page_size = GetPageSize(self)
            sx = 0.1
            sy = 0.75
            ex = 0.1
            ey = 0.25
            swipe_up(self, page_size, sx, sy, ex, ey)
            # 点击门店入库
            self.click_element(deLocation.stock_in)
            # 点击调拨入库
            self.click_element(deLocation.delivery_receive)
            # 点击高级搜索
            self.click_element(deLocation.order_search)
            # 输入调拨单号
            self.input_element(deLocation.search_order_no, transferin_order)
            # 输入商品编码
            self.input_element(deLocation.search_order_sku, sku)
            # 点击调拨类型
            self.click_element(deLocation.type_edit)
            page_size = GetPageSize(self)
            sx = 0.5
            sy = 0.75
            ex = 0.5
            ey = 0.80
            swipe_up(self, page_size, sx, sy, ex, ey)
            self.click_element(deLocation.transfer_options_submit)
            # 点击查询
            self.click_element(deLocation.search_query)
            self.click_element(basePage.menu_btn_layout)

            swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
            self.click_element(basePage.logout)
            self.click_element(basePage.text_confirm)
        except Exception as e:
            raise Exception('调拨入库单高级搜索出现异常:%s'%e)
