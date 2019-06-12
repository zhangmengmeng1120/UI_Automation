#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from android_page_location import inventoryLocation as inLocation
from android_page_location import basePage
import time
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Inventory(BaseFunction):
    def __init__(self,driver):
        BaseFunction.__init__(self,driver)

    # 全盘
    def inventory_create(self,business,username,password,rack_name):
        '''
        创建盘点单
        :return:
        '''
        basePage.login(self,business,username,password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            time.sleep(2)
            if not update_info: break
        self.click_element(basePage.menu_btn_layout)
        self.click_element(inLocation.module_item_name)
        processing = self.find_element(inLocation.inventory_details_cancel_btn)
        if processing:
            self.click_element(inLocation.inventory_details_cancel_btn)
        self.click_element(inLocation.stock_list_add_btn)
        self.click_element(inLocation.new_inventory_submit_btn)
        self.click_element(inLocation.add_rack)
        rack_names = random.randint(1,999999)
        self.input_element(inLocation.rack_name,rack_names)
        self.click_element(inLocation.text_confirm)


    def inventory_filtrate(self):
        '''
        根据盘点单状态筛选盘点单
        :return:
        '''






    def inventory_query(self):
        '''
        盘点单高级搜索
        :return:
        '''

