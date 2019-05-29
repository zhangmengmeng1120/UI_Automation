#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from ios_page_location import basePage
from h5_page_location import reportLocation as reLocation
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')


class Report(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def basic_report_act(self, business, username, password):
        basePage.login(self, business, username, password)
        time.sleep(6)
        try:
            self.click_acc(basePage.menu)
            time.sleep(2)
            self.click_acc(basePage.report_item_name)
            time.sleep(2)
            contexts = self.driver.contexts
            print contexts
            self.switch_h5(contexts[1])
            time.sleep(4)

            for x in reLocation.all_reports:
                self.click_element(x, timeout=4)
                self.click_element(reLocation.report_search_button, timeout=6)
                self.click_element(reLocation.menu_back_button, timeout=6)

        except Exception as e:
            print e
            raise Exception('报表查询操作出现异常')

    def shop_inventory(self, business, username, password):
        basePage.login(self, business, username, password)
        try:
            self.click_acc(basePage.menu)
            self.click_acc(basePage.report_item_name)
            contexts = self.driver.contexts
            self.driver.switch_to.context(contexts[1])
            time.sleep(4)
            self.click_element(reLocation.shop_inventory_button, timeout=4)
            self.click_element(reLocation.report_search_button, timeout=6)
        except Exception as e:
            print e
            raise Exception('报表查询操作出现异常')

    def shop_inventory_diff(self, business, username, password):
        basePage.login(self, business, username, password)
        try:
            self.click_acc(basePage.menu)
            self.click_acc(basePage.report_item_name)
            contexts = self.driver.contexts
            self.driver.switch_to.context(contexts[1])
            time.sleep(4)
            self.click_element(reLocation.shop_inventory_diff_button, timeout=4)
            self.click_element(reLocation.report_search_button, timeout=6)
        except:
            raise Exception('报表查询操作出现异常')
