#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from ios_page_location import basePage
import time
from ios_page_location import cloudOrderLocation as coLocation

class CloudOrder(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def basic_cloud_act(self, business, username, password, product_codes):
        basePage.login(self, business, username, password)
        self.click_acc(basePage.menu)
        time.sleep(4)
        self.click_acc(basePage.cloud_order_item)
        # try:

        # ===================>>>>>>>我的云单<<<<<<<<===============================
        self.order_list()

        # except Exception as e:
        #     raise Exception('云仓订单操作出现异常')

    # 我的云单
    def order_list(self):
        self.click_acc(basePage.self_cloud_item)

        self.click_acc(coLocation.order_state_title)
        self.click_acc(coLocation.distributed_order_state)

        self.click_acc(coLocation.distributed_order_state)
        self.click_acc(coLocation.ready_order_state)

        self.click_acc(coLocation.ready_order_state)
        self.click_acc(coLocation.transfered_order_state)

        self.click_acc(coLocation.transfered_order_state)
        # self.click_acc(coLocation.canceled_order_state)




