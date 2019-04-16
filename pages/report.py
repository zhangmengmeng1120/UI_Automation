#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from basePage import login, swipe_up, GetPageSize
from page_location import reportLocation as reLocation
import basePage
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')


class Report(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def basic_report_act(self, business, username, password):
        login(self, business, username, password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            time.sleep(2)
            if not update_info: break
        try:
            self.click_element(basePage.menu_btn_layout)
            self.click_element(reLocation.module_item_name, timeout=4)
            contexts = self.driver.contexts
            self.driver.switch_to.context(contexts[1])
            time.sleep(4)

            for x in reLocation.all_reports:
                self.click_element(x, timeout=4)
                self.click_element(reLocation.report_search_button, timeout=6)
                self.click_element(reLocation.menu_back_button, timeout=6)
                print x

        except Exception as e:
            print e
            raise Exception('报表查询操作出现异常')

    def shop_inventory(self, business, username, password):
        login(self, business, username, password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            time.sleep(2)
            if update_info == False: break
        try:
            self.click_element(basePage.menu_btn_layout)
            self.click_element(reLocation.module_item_name, timeout=4)
            contexts = self.driver.contexts
            self.driver.switch_to.context(contexts[1])
            time.sleep(4)
            self.click_element(reLocation.shop_inventory_button, timeout=4)
            self.click_element(reLocation.report_search_button, timeout=6)
        except Exception as e:
            print e
            raise Exception('报表查询操作出现异常')

    def shop_inventory_diff(self, business, username, password):
        login(self, business, username, password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            time.sleep(2)
            if update_info == False: break
        try:
            self.click_element(basePage.menu_btn_layout)
            self.click_element(reLocation.module_item_name, timeout=4)
            contexts = self.driver.contexts
            self.driver.switch_to.context(contexts[1])
            time.sleep(4)
            self.click_element(reLocation.shop_inventory_diff_button, timeout=4)
            self.click_element(reLocation.report_search_button, timeout=6)
        except:
            raise Exception('报表查询操作出现异常')
