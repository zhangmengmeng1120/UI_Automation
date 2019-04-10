#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from basePage import login,swipe_up,GetPageSize
import bestSellingLocation as bsl
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
        time.sleep(40)
        while True:
            update_info = self.find_element(bsl.update_text_info)
            print update_info
            time.sleep(2)
            if update_info==False: break

        # try:
        self.click_element(basePage.menu_btn_layout)
        # page_size = GetPageSize(self)
        # swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
        # self.click_element(basePage.settings)
        # self.click_element(basePage.update_data)
        # self.click_element(basePage.system_cache_clear_tv)
        # self.click_element(basePage.text_confirm)
        # self.click_element(basePage.menu_btn_layout)
        # downs_x = 0.1
        # downs_y = 0.25
        # downe_x = 0.1
        # downe_y = 0.62
        # # 下拉刷新
        # swipe_up(self, GetPageSize(self), downs_x, downs_y, downe_x, downe_y)
        self.click_element(bsl.module_item_name)
        self.click_element(bsl.favourite_product)
        self.driver.find_element_by_accessibility_id('同城库存').click()
        time.sleep(2)
        # 向上滑动页面
        page_size = GetPageSize(self)
        print page_size
        sx = 0.1
        sy = 0.75
        ex = 0.1
        ey = 0.25
        swipe_up(self,page_size,sx,sy,ex,ey)
        self.click_element(bsl.back_btn)
        # self.click_element(bsl.search_product_btn)
        self.driver.tap([(1900,100)])
        self.input_element(bsl.search_edit_text,product_code)
        self.driver.find_element_by_accessibility_id("搜索").click()
        self.click_element(bsl.searcg_product)
        self.click_element(basePage.menu_btn_layout)
        page_size = GetPageSize(self)
        swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
        self.click_element(basePage.logout)
        self.click_element(basePage.text_confirm)
        # except:
        #     raise Exception('畅销排行操作出现异常')




