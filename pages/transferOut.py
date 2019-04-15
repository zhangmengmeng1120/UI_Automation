#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from basePage import login, swipe_up, GetPageSize
import basePage
import time
from page_location import transferOutLocation as tranLocation

class TransferOut(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def transfer_out_create(self,business,username,password):
        product_code = ['1821012','1721001']
        login(self,business,username,password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            print update_info
            time.sleep(2)
            if update_info == False: break
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
        self.click_element(tranLocation.stock_out)
        # 点击调拨出库
        self.click_element(tranLocation.transfer_out)
        time.sleep(5)
        self.click_element(tranLocation.allocate_add)
        self.click_element(tranLocation.shop_edit)
        self.click_element(tranLocation.change_shop)
        self.click_element(tranLocation.type_edit)
        self.click_element(tranLocation.change_stock)
        self.click_element(tranLocation.et_allocate_reason)
        self.click_element(tranLocation.change_reason)
        self.click_element(tranLocation.allocate_next)
        time.sleep(6)
        contexts = self.driver.contexts
        self.switch_h5(contexts[1])
        time.sleep(4)
        self.click_element(tranLocation.add_handle)
        time.sleep(4)
        for code in product_code:
            contexts = self.driver.contexts
            self.switch_h5(contexts[0])
            time.sleep(7)
            self.click_element(tranLocation.search_product)
            for num in code:
                self.driver.press_keycode(basePage.keycode[num])
            self.click_element(basePage.keypad_search_btn)
            contexts = self.driver.contexts
            self.switch_h5(contexts[1])
            time.sleep(4)
            self.click_element(tranLocation.product_colors)
            self.click_element(tranLocation.product_size)
            self.click_element(tranLocation.add)
        self.click_element(tranLocation.back_btn)
        print self.driver.page_source
        self.click_element(tranLocation.confirm)
        self.click_element(tranLocation.back_btn)
        contexts = self.driver.contexts
        self.switch_h5(contexts[0])
        time.sleep(6)
        self.click_element(basePage.menu_btn_layout)
        page_size = GetPageSize(self)
        swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
        self.click_element(basePage.logout)
        self.click_element(basePage.text_confirm)


