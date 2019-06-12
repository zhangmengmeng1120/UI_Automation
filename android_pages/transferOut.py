#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from android_page_location import basePage
import time
from android_page_location import transferOutLocation as tranLocation

class TransferOut(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    # 调拨出库单创建
    def transfer_out_create(self,business,username,password,product_codes):
        basePage.login(self,business,username,password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            time.sleep(2)
            if not update_info: break
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
            for code in product_codes:
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
            self.click_element(tranLocation.confirm)
            self.click_element(tranLocation.back_btn)
            contexts = self.driver.contexts
            self.switch_h5(contexts[0])
            time.sleep(6)
            self.click_element(basePage.menu_btn_layout)
            page_size = basePage.GetPageSize(self)
            basePage.swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
            self.click_element(basePage.logout)
            self.click_element(basePage.text_confirm)
        except Exception as e:
            raise Exception('创建调拨单时出现异常:%s'%e)

    # 提交出库
    def transfer_out_upload(self,business,username,password,product_codes):
        basePage.login(self,business,username,password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            time.sleep(2)
            if not update_info: break
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

            # 点击门店出库
            self.click_element(tranLocation.stock_out)
            # 点击调拨出库
            self.click_element(tranLocation.transfer_out)
            time.sleep(5)
            self.click_element(tranLocation.title)
            self.click_element(tranLocation.draft_order)
            self.click_element(tranLocation.confirm_allocate_txt)
            el = self.find_element(tranLocation.confirm_tip)
            if el:
                self.click_element(tranLocation.text_confirm)
                self.click_element(tranLocation.details_text)
                contexts = self.driver.contexts
                self.switch_h5(contexts[1])
                time.sleep(7)
                self.click_element(tranLocation.add_handle)
                time.sleep(4)
                for code in product_codes:
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
                self.click_element(tranLocation.confirm)
                self.click_element(tranLocation.back_btn)
                time.sleep(1)
                contexts = self.driver.contexts
                self.switch_h5(contexts[0])
                time.sleep(6)
                self.click_element(tranLocation.confirm_allocate_txt)
                self.click_element(tranLocation.allocate_next)
                time.sleep(1)
                self.click_element(tranLocation.allocate_next)
                time.sleep(2)
                self.click_element(basePage.menu_btn_layout)
                page_size = basePage.GetPageSize(self)
                basePage.swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
                self.click_element(basePage.logout)
                self.click_element(basePage.text_confirm)

            else:
                self.click_element(tranLocation.text_confirm)
                self.click_element(tranLocation.allocate_next)
                time.sleep(1)
                self.click_element(tranLocation.allocate_next)
                time.sleep(2)
                self.click_element(basePage.menu_btn_layout)
                page_size = basePage.GetPageSize(self)
                basePage.swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
                self.click_element(basePage.logout)
                self.click_element(basePage.text_confirm)
        except Exception as e:
            raise Exception('提交调拨出库出现异常%s'%e)


    def transferout_by_orderno(self, business, username, password, transferin_order, sku):
        '''
        调拨入库单高级搜索,根据调拨单号进行模糊搜索
        :return:
        '''
        # 登录
        basePage.login(self, business, username, password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            time.sleep(2)
            if not update_info: break
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
            self.click_element(tranLocation.stock_out)
            # 点击调拨入库
            self.click_element(tranLocation.transfer_out)
            # 点击高级搜索
            self.click_element(tranLocation.order_search)
            # 输入调拨单号
            self.input_element(tranLocation.search_order_no, transferin_order)
            # 输入商品编码
            self.input_element(tranLocation.search_order_sku, sku)
            # 点击调拨类型
            # self.click_element(tranLocation.type_edit)
            page_size = basePage.GetPageSize(self)
            sx = 0.5
            sy = 0.75
            ex = 0.5
            ey = 0.80
            basePage.swipe_up(self, page_size, sx, sy, ex, ey)
            # 点击查询
            self.click_element(tranLocation.search_query)
            time.sleep(2)
            self.click_element(basePage.menu_btn_layout)

            basePage.swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
            self.click_element(basePage.logout)
            self.click_element(basePage.text_confirm)
        except Exception as e:
            raise Exception('调拨出库单高级搜索出现异常:%s'%e)