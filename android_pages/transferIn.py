#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from android_page_location import basePage
from android_page_location import transferInLocation as tranLocation
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class TransferIn(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def transfer_confirm(self, business, username, password):
        '''
        签收待签收的单据
        :param business:
        :param username:
        :param password:
        :return:
        '''
        basePage.login(self, business, username, password)
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
            page_size = basePage.GetPageSize(self)
            sx = 0.1
            sy = 0.75
            ex = 0.1
            ey = 0.25
            basePage.swipe_up(self, page_size, sx, sy, ex, ey)

            # 点击门店入库
            self.click_element(tranLocation.stock_in)
            # 点击调拨入库
            self.click_element(tranLocation.transfer_in)
            time.sleep(5)
            self.click_element(tranLocation.details_text)
            contexts = self.driver.contexts
            self.switch_h5(contexts[1])
            time.sleep(4)
            self.click_element(tranLocation.icon_edit)
            self.click_element(tranLocation.icon_delete)
            self.click_element(tranLocation.num_key)
            self.click_element(tranLocation.key_confirm)
            self.click_element(tranLocation.btn_save)
            self.click_element(tranLocation.back_btn)
            time.sleep(4)
            contexts = self.driver.contexts
            self.switch_h5(contexts[0])
            time.sleep(2)
            self.click_element(tranLocation.take_receive)
            el = self.find_element(tranLocation.transfer_diff_wizard)
            if el:
                self.click_element(tranLocation.diff_confirm_button)
                time.sleep(3)
            self.click_element(tranLocation.text_confirm_button)
            time.sleep(1)
        except:
            raise Exception('签收调拨单出现异常')
        self.click_element(basePage.menu_btn_layout)
        page_size = basePage.GetPageSize(self)
        basePage.swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
        self.click_element(basePage.logout)
        self.click_element(basePage.text_confirm)

    def transfer_by_orderno(self, business, username, password, transferin_order, sku):
        '''
        调拨入库单高级搜索,根据调拨单号进行模糊搜索
        :return:
        '''
        # 登录
        basePage.login(self, business, username, password)
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
            page_size = basePage.GetPageSize(self)
            sx = 0.1
            sy = 0.75
            ex = 0.1
            ey = 0.25
            basePage.swipe_up(self, page_size, sx, sy, ex, ey)
            # 点击门店入库
            self.click_element(tranLocation.stock_in)
            # 点击调拨入库
            self.click_element(tranLocation.transfer_in)
            # 点击高级搜索
            self.click_element(tranLocation.order_search)
            # 输入调拨单号
            self.input_element(tranLocation.search_order_no, transferin_order)
            # 输入商品编码
            self.input_element(tranLocation.search_order_sku, sku)
            # 点击调拨类型
            self.click_element(tranLocation.type_edit)
            page_size = basePage.GetPageSize(self)
            sx = 0.5
            sy = 0.75
            ex = 0.5
            ey = 0.80
            basePage.swipe_up(self, page_size, sx, sy, ex, ey)
            self.click_element(tranLocation.transfer_options_submit)
            # 点击查询
            self.click_element(tranLocation.search_query)
            self.click_element(basePage.menu_btn_layout)

            basePage.swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
            self.click_element(basePage.logout)
            self.click_element(basePage.text_confirm)
        except Exception as e:
            raise Exception('调拨入库单高级搜索出现异常:%s'%e)
