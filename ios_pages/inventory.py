#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from ios_page_location import basePage
from ios_page_location import inventoryLocation as invenLocation
from h5_pages import h5_order
import time


class StockInventory(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    # ===================>>>>>>>创建盘点单盘点<<<<<<<<===============================
    def inventory_create(self, business, username, password,product_codes):

        basePage.login(self,business, username, password)
        time.sleep(7)
        print self.driver.page_source
        self.click_acc(basePage.menu)
        time.sleep(1)
        self.click_acc(invenLocation.menu_info)
        time.sleep(2)
        if self.find_element_by_accessibility_id(invenLocation.inven_cancel):
            self.click_acc(invenLocation.inven_cancel)
        time.sleep(1)
        # 确认取消盘点
        self.click_acc(basePage.update_confirm)
        time.sleep(4)
        self.click_acc(invenLocation.add_btn)
        time.sleep(1)
        self.click_acc(invenLocation.add)
        time.sleep(2)
        self.click_acc(invenLocation.add_goods_shelves)
        time.sleep(2)
        self.input_element(invenLocation.rack_name,basePage.get_rack_name())
        time.sleep(1)
        self.click_acc(basePage.disappear_keyboard)
        time.sleep(1)
        self.click_element(invenLocation.stock_name)
        time.sleep(1)
        self.click_acc(invenLocation.stock_type)
        time.sleep(1)
        self.click_acc(invenLocation.rack_confirm)
        time.sleep(5)
        h5_order.add_product(self,product_codes)

    # ===================>>>>>>>盘点单高级搜索<<<<<<<<===============================
    def inventory_query(self, business, username, password):
        basePage.login(self, business, username, password)
        time.sleep(7)
        self.click_acc(basePage.menu)
        time.sleep(1)
        self.click_acc(invenLocation.menu_info)
        time.sleep(2)
        self.click_acc(basePage.search_advanced)
        time.sleep(2)

    # ===================>>>>>>>盘点，查看盘点差异<<<<<<<<===============================
    def inventory_read_diff(self, business, username, password):
        basePage.login(self, business, username, password)
        time.sleep(7)
        self.click_acc(basePage.menu)
        time.sleep(1)
        self.click_acc(invenLocation.menu_info)
        time.sleep(1)
        if self.find_element_by_accessibility_id(invenLocation.inven_cancel):
            self.click_acc(invenLocation.inven_diff)


