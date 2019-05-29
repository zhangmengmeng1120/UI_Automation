#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from basePage import login, swipe_up, GetPageSize
import basePage
import time
from android_page_location import cloudOrderLocation as coLocation

class CloudOrder(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def basic_cloud_act(self, business, username, password, product_codes):
        login(self, business, username, password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            time.sleep(2)
            if not update_info: break
        try:

            self.click_element(basePage.menu_btn_layout)

            page_size = GetPageSize(self)
            sx = 0.1
            sy = 0.75
            ex = 0.1
            ey = 0.25
            swipe_up(self, page_size, sx, sy, ex, ey)
            self.click_element(coLocation.module_item_name, timeout=1)

            # ===================>>>>>>>我的云单<<<<<<<<===============================
            self.order_list()
            # ===================>>>>>>>门店指标<<<<<<<<===============================

        except Exception as e:
            raise Exception('报表查询操作出现异常')

    # 我的云单
    def order_list(self):
        self.click_element(coLocation.my_cloud_order_item, timeout=4)

        self.click_element(coLocation.order_state_title)
        self.click_element(coLocation.distributed_order_state, timeout=4)

        self.click_element(coLocation.order_state_title)
        self.click_element(coLocation.ready_order_state, timeout=4)

        self.click_element(coLocation.order_state_title)
        self.click_element(coLocation.transfered_order_state, timeout=4)

        self.click_element(coLocation.order_state_title)
        self.click_element(coLocation.canceled_order_state, timeout=4)




