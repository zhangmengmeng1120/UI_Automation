#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from basePage import login,swipe_up,GetPageSize
from page_location import bestSellingLocation as bsLocation
import basePage
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')


class BestSelling(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)


    def best_info(self, business, username, password,product_code):
        login(self, business, username, password)
        self.driver.wait_activity(".bash.ui.MainActivity",10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            print update_info
            time.sleep(2)
            if update_info==False: break

        try:
            self.click_element(basePage.menu_btn_layout)
            self.click_element(bsLocation.module_item_name)
            time.sleep(5)
            contexts = self.driver.contexts
            self.switch_h5(contexts[1])
            time.sleep(4)
            self.click_element(bsLocation.search_product_btn)
            self.input_element(bsLocation.input_product,product_code)
            self.click_element(bsLocation.search)
            time.sleep(2)
            self.click_element(bsLocation.clear)
            self.click_element(bsLocation.cancel)
            el = self.find_element(bsLocation.favourite_product)
            if el:
                self.click_element(bsLocation.favourite_product)
                time.sleep(5)
                self.click_element(bsLocation.inventory)
                time.sleep(2)
                self.click_element(bsLocation.back_btn)
            contexts = self.driver.contexts
            self.switch_h5(contexts[0])
            time.sleep(5)
            self.click_element(basePage.menu_btn_layout)
            page_size = GetPageSize(self)
            swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
            self.click_element(basePage.logout)
            self.click_element(basePage.text_confirm)
        except:
            raise Exception('畅销排行操作出现异常')




