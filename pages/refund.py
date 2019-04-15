#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from basePage import login, swipe_up, GetPageSize
import basePage
import time
from page_location import refundLocation as reLocation

class Refund(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    # 调拨出库单创建
    def refund_create(self,business,username,password,product_codes):
        login(self,business,username,password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            time.sleep(2)
            if not update_info: break
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

            # 点击门店出库
            self.click_element(reLocation.stock_out)
            # 点击配货退货
            self.click_element(reLocation.refund)
            time.sleep(5)
            self.click_element(reLocation.allocate_add)
            self.click_element(reLocation.store_in_name)
            self.click_element(reLocation.change_shop)
            self.click_element(reLocation.store_reason)
            self.click_element(reLocation.change_reason)
            self.click_element(reLocation.stock_confirm)
            time.sleep(6)
            contexts = self.driver.contexts
            self.switch_h5(contexts[1])
            time.sleep(4)
            self.click_element(reLocation.add_handle)
            time.sleep(4)
            for code in product_codes:
                contexts = self.driver.contexts
                self.switch_h5(contexts[0])
                time.sleep(7)
                self.click_element(reLocation.search_product)
                for num in code:
                    self.driver.press_keycode(basePage.keycode[num])
                self.click_element(basePage.keypad_search_btn)
                contexts = self.driver.contexts
                self.switch_h5(contexts[1])
                time.sleep(4)
                self.click_element(reLocation.product_colors)
                self.click_element(reLocation.product_size)
                self.click_element(reLocation.add)
            self.click_element(reLocation.back_btn)
            self.click_element(reLocation.confirm)
            self.click_element(reLocation.back_btn)
            contexts = self.driver.contexts
            self.switch_h5(contexts[0])
            time.sleep(6)
            self.click_element(basePage.menu_btn_layout)
            page_size = GetPageSize(self)
            swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
            self.click_element(basePage.logout)
            self.click_element(basePage.text_confirm)
        except Exception as e:
            raise Exception('创建调拨单时出现异常:%s'%e)

    # 提交出库
    def refund_upload(self,business,username,password,product_codes):
        login(self,business,username,password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            time.sleep(2)
            if not update_info: break
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
            # 点击门店出库
            self.click_element(reLocation.stock_out)
            # 点击配货退货
            self.click_element(reLocation.refund)
            time.sleep(5)
            self.click_element(reLocation.title)
            self.click_element(reLocation.draft_order)
            self.click_element(reLocation.confirm_return_txt)
            el = self.find_element(reLocation.confirm_tip)
            if el:
                contexts = self.driver.contexts
                self.switch_h5(contexts[1])
                time.sleep(7)
                self.click_element(reLocation.add_handle)
                time.sleep(4)
                for code in product_codes:
                    contexts = self.driver.contexts
                    self.switch_h5(contexts[0])
                    time.sleep(7)
                    self.click_element(reLocation.search_product)
                    for num in code:
                        self.driver.press_keycode(basePage.keycode[num])
                    self.click_element(basePage.keypad_search_btn)
                    contexts = self.driver.contexts
                    self.switch_h5(contexts[1])
                    time.sleep(4)
                    self.click_element(reLocation.product_colors)
                    self.click_element(reLocation.product_size)
                    self.click_element(reLocation.add)
                self.click_element(reLocation.back_btn)
                self.click_element(reLocation.confirm)
                self.click_element(reLocation.back_btn)
                time.sleep(1)
                contexts = self.driver.contexts
                self.switch_h5(contexts[0])
                time.sleep(6)
                self.click_element(reLocation.confirm_return_txt)
                time.sleep(2)
                self.click_element(reLocation.send_btn)
                time.sleep(1)
                self.click_element(basePage.menu_btn_layout)
                page_size = GetPageSize(self)
                swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
                self.click_element(basePage.logout)
                self.click_element(basePage.text_confirm)
            else:
                self.click_element(reLocation.allocate_next)
                time.sleep(2)
                self.click_element(reLocation.title)
                self.click_element(reLocation.waiting_order)
                time.sleep(1)
                self.click_element(reLocation.send_btn)
                time.sleep(2)
                self.click_element(basePage.menu_btn_layout)
                page_size = GetPageSize(self)
                swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
                self.click_element(basePage.logout)
                self.click_element(basePage.text_confirm)
        except Exception as e:
            raise Exception('提交退货单出现异常%s'%e)


    def refund_by_orderno(self, business, username, password, transferin_order, sku):
        '''
        调拨入库单高级搜索,根据调拨单号进行模糊搜索
        :return:
        '''
        # 登录
        login(self, business, username, password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            time.sleep(2)
            if not update_info: break
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
            # 点击配货退货
            self.click_element(reLocation.stock_out)
            # 点击入库
            self.click_element(reLocation.refund)
            # 点击高级搜索
            self.click_element(reLocation.order_search)
            # 输入退货单号
            self.input_element(reLocation.search_order_no, transferin_order)
            # 输入商品编码
            self.input_element(reLocation.search_order_sku, sku)
            # 点击查询
            self.click_element(reLocation.search_query)
            self.click_element(basePage.menu_btn_layout)
            time.sleep(2)
            swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
            self.click_element(basePage.logout)
            self.click_element(basePage.text_confirm)
        except Exception as e:
            raise Exception('配货退货单高级搜索出现异常:%s'%e)