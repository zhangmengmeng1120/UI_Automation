#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
import basePage
from basePage import login, GetPageSize, swipe_up
from android_page_location import reloadLocation as reLocation
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class Reload(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def basic_reload_act(self, business, username, password, product_codes):
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
            self.click_element(reLocation.module_item_name, timeout=1)

            # ===================>>>>>>>我的云单<<<<<<<<===============================
            self.apply_reload(product_codes)

            self.click_element(reLocation.reload_state_choice, timeout=1)
            self.click_element(reLocation.draft_reload, timeout=1)
            self.click_element(reLocation.commit_reload_button, timeout=1)
            self.click_element(reLocation.conform_commit, timeout=3)
            self.click_element(reLocation.cancel_reload_button, timeout=3)
            self.click_element(reLocation.conform_commit, timeout=3)


            self.click_element(reLocation.reload_state_choice, timeout=1)
            self.click_element(reLocation.approve_reload, timeout=1)

            self.click_element(reLocation.reload_state_choice, timeout=1)
            self.click_element(reLocation.waiting_reload, timeout=1)

            self.click_element(reLocation.reload_state_choice, timeout=1)
            self.click_element(reLocation.done_reload, timeout=1)

            self.click_element(reLocation.reload_state_choice, timeout=1)
            self.click_element(reLocation.reject_reload, timeout=1)
            self.click_element(reLocation.commit_reload_button, timeout=1)
            self.click_element(reLocation.conform_commit, timeout=3)

            self.click_element(reLocation.cancel_reload_button, timeout=3)
            self.click_element(reLocation.conform_commit, timeout=3)

            self.click_element(reLocation.reload_state_choice, timeout=1)
            self.click_element(reLocation.cancel_reload, timeout=1)


        except Exception as e:
            raise Exception('报表查询操作出现异常')

    def apply_reload(self, product_codes):
        self.click_element(reLocation.reload_apply_item_name, timeout=2)

        contexts = self.driver.contexts
        self.switch_h5(contexts[1])

        self.click_element(reLocation.add_new_reload, timeout=1)

        self.click_element(reLocation.shop_transfer_button, timeout=1)
        self.click_element(reLocation.choose_shop)
        self.click_element(reLocation.first_shop, timeout=1)
        self.click_element(reLocation.next_step, timeout=1)

        self.click_element(reLocation.add_product, timeout=1)
        for code in product_codes:
            contexts = self.driver.contexts
            self.switch_h5(contexts[0])
            time.sleep(7)
            self.click_element(reLocation.search_product)
            for num in code:
                self.driver.press_keycode(basePage.keycode[num])
            self.click_element(basePage.keypad_search_btn)
            contexts = self.driver.contexts
            self.switch_h5(contexts[1])
            time.sleep(4)
            self.click_element(reLocation.product_colors)
            self.click_element(reLocation.product_size)
            self.click_element(reLocation.add)

        self.click_element(reLocation.back_btn)
        self.click_element(reLocation.confirm)
        self.click_element(reLocation.back_btn)
