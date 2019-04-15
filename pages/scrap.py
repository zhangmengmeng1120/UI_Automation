#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from basePage import login, swipe_up, GetPageSize
import basePage
import time
from page_location import scrapLocation as sLocation

class Scrap(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    # 损益单创建
    def scrap_create(self,business,username,password,product_codes):
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
            # 点击库存损益
            self.click_element(sLocation.scrap)
            time.sleep(5)
            self.click_element(sLocation.stock_loss_add)
            self.click_element(sLocation.product_type_edit)
            self.click_element(sLocation.change_product)
            self.click_element(sLocation.stock_type_edit)
            self.click_element(sLocation.change_reason)
            self.input_element(sLocation.resean_edit,'123')
            self.click_element(sLocation.stock_loss_next)
            time.sleep(6)
            contexts = self.driver.contexts
            self.switch_h5(contexts[1])
            time.sleep(4)
            self.click_element(sLocation.add_handle)
            time.sleep(4)
            for code in product_codes:
                contexts = self.driver.contexts
                self.switch_h5(contexts[0])
                time.sleep(7)
                self.click_element(sLocation.search_product)
                for num in code:
                    self.driver.press_keycode(basePage.keycode[num])
                self.click_element(basePage.keypad_search_btn)
                contexts = self.driver.contexts
                self.switch_h5(contexts[1])
                time.sleep(4)
                self.click_element(sLocation.product_colors)
                self.click_element(sLocation.product_size)
                self.click_element(sLocation.add)
            self.click_element(sLocation.back_btn)
            self.click_element(sLocation.confirm)
            self.click_element(sLocation.back_btn)
            contexts = self.driver.contexts
            self.switch_h5(contexts[0])
            time.sleep(6)
            self.click_element(basePage.menu_btn_layout)
            page_size = GetPageSize(self)
            swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
            self.click_element(basePage.logout)
            self.click_element(basePage.text_confirm)
        except Exception as e:
            raise Exception('创建损益单时出现异常:%s'%e)

    # 提交出库
    def scrap_upload(self,business,username,password,product_codes):
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

            # 点击库存损益
            self.click_element(sLocation.scrap)
            time.sleep(5)
            self.click_element(sLocation.title)
            self.click_element(sLocation.draft_order)
            self.click_element(sLocation.confirm_stock_loss_txt)
            el = self.find_element(sLocation.confirm_tip)
            if el:
                self.click_element(sLocation.text_confirm)
                self.click_element(sLocation.details_text)
                contexts = self.driver.contexts
                self.switch_h5(contexts[1])
                time.sleep(7)
                self.click_element(sLocation.add_handle)
                time.sleep(4)
                for code in product_codes:
                    contexts = self.driver.contexts
                    self.switch_h5(contexts[0])
                    time.sleep(7)
                    self.click_element(sLocation.search_product)
                    for num in code:
                        self.driver.press_keycode(basePage.keycode[num])
                    self.click_element(basePage.keypad_search_btn)
                    contexts = self.driver.contexts
                    self.switch_h5(contexts[1])
                    time.sleep(4)
                    self.click_element(sLocation.product_colors)
                    self.click_element(sLocation.product_size)
                    self.click_element(sLocation.add)
                self.click_element(sLocation.back_btn)
                self.click_element(sLocation.confirm)
                self.click_element(sLocation.back_btn)
                time.sleep(1)
                contexts = self.driver.contexts
                self.switch_h5(contexts[0])
                time.sleep(6)
                self.click_element(sLocation.confirm_stock_loss_txt)
                time.sleep(1)
                self.click_element(sLocation.text_confirm)
                self.click_element(basePage.menu_btn_layout)
                page_size = GetPageSize(self)
                swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
                self.click_element(basePage.logout)
                self.click_element(basePage.text_confirm)
            else:
                self.click_element(sLocation.text_confirm)
                time.sleep(2)
                self.click_element(basePage.menu_btn_layout)
                page_size = GetPageSize(self)
                swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
                self.click_element(basePage.logout)
                self.click_element(basePage.text_confirm)
        except Exception as e:
            raise Exception('提交损益出现异常%s'%e)


    def scrap_by_orderno(self, business, username, password, transferin_order, sku):
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
            # 点击库存损益
            self.click_element(sLocation.scrap)
            # 点击高级搜索
            self.click_element(sLocation.order_search)
            # 输入退货单号
            self.input_element(sLocation.search_order_no, transferin_order)
            # 输入商品编码
            self.input_element(sLocation.search_order_sku, sku)
            # 点击查询
            self.click_element(sLocation.search_query)
            time.sleep(1)
            self.click_element(basePage.menu_btn_layout)
            time.sleep(2)
            swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
            self.click_element(basePage.logout)
            self.click_element(basePage.text_confirm)
        except Exception as e:
            raise Exception('损益单高级搜索出现异常:%s'%e)