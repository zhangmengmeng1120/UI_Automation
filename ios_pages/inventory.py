#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from ios_page_location import basePage
from ios_page_location import inventoryLocation as invenLocation
from h5_page_location import h5OrderLocation
from h5_pages import h5_order
import time


class StockInventory(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    # ===================>>>>>>>创建盘点单盘点<<<<<<<<===============================
    def inventory_create(self, business, username, password,product_codes):

        basePage.login(self,business, username, password)
        self.click_acc(basePage.menu)
        self.click_acc(invenLocation.menu_info)
        if self.find_element_by_accessibility_id(invenLocation.inven_cancel):
            self.click_acc(invenLocation.inven_cancel)
        # 确认取消盘点
        self.click_acc(basePage.update_confirm)
        time.sleep(2)
        self.click_acc(invenLocation.add_btn)
        self.click_acc(invenLocation.add)
        time.sleep(1)
        self.click_acc(invenLocation.add_goods_shelves)
        self.input_element(invenLocation.rack_name,basePage.get_rack_name())
        self.click_acc(basePage.disappear_keyboard)
        self.click_element(invenLocation.stock_name)
        self.click_acc(invenLocation.stock_type)
        self.click_acc(invenLocation.rack_confirm)
        time.sleep(3)
        h5_order.add_product(self,product_codes,'order')

    # ===================>>>>>>>盘点单高级搜索,根据单号<<<<<<<<===============================
    def inventory_query(self, business, username, password):
        basePage.login(self, business, username, password)
        self.click_acc(basePage.menu)
        self.click_acc(invenLocation.menu_info)
        basePage.search_advanced_receipts(self,1,'inventory')

    # ===================>>>>>>>盘点，查看盘点差异<<<<<<<<===============================
    def inventory_read_diff(self, business, username, password,product_code):
        basePage.login(self, business, username, password)
        self.click_acc(basePage.menu)
        self.click_acc(invenLocation.menu_info)
        if self.find_element_by_accessibility_id(invenLocation.inven_cancel):
            self.click_acc(invenLocation.inven_diff)
            time.sleep(2)
            contexts = self.driver.contexts
            self.switch_h5(contexts[1])
            self.click_element(h5OrderLocation.link_by_num)
            time.sleep(4)
            contexts = self.driver.contexts
            self.switch_h5(contexts[2])
            self.click_element(h5OrderLocation.close_win)
            time.sleep(1)
            contexts = self.driver.contexts
            self.switch_h5(contexts[1])
            self.click_element(h5OrderLocation.back_btn)
            contexts = self.driver.contexts
            self.switch_h5(contexts[0])
            self.click_acc(invenLocation.detail)
            time.sleep(2)
            self.click_element(invenLocation.detail_sku)
            time.sleep(2)
            contexts = self.driver.contexts
            self.switch_h5(contexts[2])
            self.click_element(h5OrderLocation.close_win)




