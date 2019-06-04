#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from ios_page_location import basePage
from ios_page_location import reloadLocation as reLocation
from h5_pages import h5_order
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Reload(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    # ===================>>>>>>>补货申请<<<<<<<<===============================

    def apply_reload(self, business, username, password, product_codes):
        basePage.login(self, business, username, password)
        # try:

        self.click_acc(basePage.menu)
        time.sleep(4)
        self.click_acc(basePage.shop_reload_item)
        self.click_acc(basePage.shop_reload_apply_item)
        self.click_acc(reLocation.add_new_reload)
        self.click_acc(reLocation.stock_default)
        self.click_element(reLocation.choose_stock)
        self.click_acc(reLocation.next_step)
        h5_order.add_product(self,product_codes,'reload')
        contexts = self.driver.contexts
        self.switch_h5(contexts[0])
        time.sleep(2)
        self.click_acc(reLocation.reload_state_choice)

        self.click_acc(reLocation.draft_reload)
        if self.find_element_by_accessibility_id(reLocation.cancel_reload_button):
            self.click_acc(reLocation.commit_reload_button)
        if self.find_element_by_accessibility_id(reLocation.cancel_reload_button):
            self.click_acc(reLocation.cancel_reload_button)
            self.click_acc(reLocation.cancel_ok)

        self.click_acc(reLocation.draft_reload)
        self.click_acc(reLocation.approve_reload)

        self.click_acc(reLocation.approve_reload)
        self.click_acc(reLocation.waiting_reload)

        self.click_acc(reLocation.waiting_reload)
        self.click_acc(reLocation.done_reload)

        self.click_acc(reLocation.done_reload)
        self.click_acc(reLocation.reject_reload)
        if self.find_element_by_accessibility_id(reLocation.cancel_reload_button):
            self.click_acc(reLocation.commit_reload_button)


        # except Exceptionon as e:
        #     raise Exception('补货单操作出现异常')

    # ===================>>>>>>>补货审批<<<<<<<<===============================

    def approve_reload(self, business, username, password):

        basePage.login(self, business, username, password)
        # try:

        self.click_acc(basePage.menu)
        time.sleep(4)
        self.click_acc(basePage.shop_reload_item)

        self.click_acc(basePage.shop_reload_approve_item)
        self.click_acc(reLocation.reload_state_choice)
        self.click_acc(reLocation.approve_reload)
        el = self.find_element_by_accessibility_id(reLocation.agree_delivery)
        if el:
            self.click_acc(reLocation.agree_delivery)
            self.click_acc(reLocation.cancel_ok)
        self.click_acc(reLocation.approve_reload)
        self.click_acc(reLocation.waiting_delivery)
        if self.find_element_by_accessibility_id(reLocation.delivery):
            self.click_acc(reLocation.delivery)
