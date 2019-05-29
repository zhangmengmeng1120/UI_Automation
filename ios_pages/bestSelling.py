#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from h5_pages import bestSelling
from ios_page_location import basePage
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')


class BestSelling(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)


    def best_info(self, business, username, password,product_code):
        basePage.login(self, business, username, password)
        time.sleep(6)
        # try:
        self.click_acc(basePage.menu)
        time.sleep(1)
        self.click_acc(basePage.best_selling)
        time.sleep(2)
        bestSelling.best_info(self,product_code)
        # except:
        #     raise Exception('畅销排行操作出现异常')




