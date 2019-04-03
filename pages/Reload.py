#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
import basePage
from basePage import login, GetPageSize, swipe_up
import TransferInLoaction as Tlocation
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TransferIn(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def create_reload_apply(self, business, username, password, product_codes):
        login(self, business, username, password)
        time.sleep(3)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
