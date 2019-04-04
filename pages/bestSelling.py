#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from basePage import login
import bestSellingLocation as bsl
import basePage
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')


class BestSelling(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)


    def best_info(self, business, username, password):
        login(self, business, username, password)
        self.click_element(basePage.menu_btn_layout)
        self.click_element(bsl.module_item_name)
        self.driver.find_element_by_accessibility_id('09275990927599599排名 4').click()
        self.driver.find_element_by_accessibility_id('同城库存').click()
        time.sleep(2)


