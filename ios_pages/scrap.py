#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from ios_page_location import basePage
import time
from ios_page_location import scrapLocation as sLocation
from h5_pages import h5_order
import random

class Scrap(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def normal(self,business,username,password):
        basePage.login(self, business, username, password)
        self.click_acc(basePage.menu)
        time.sleep(5)
        self.click_acc(basePage.shop_scrap)
    # 损益单创建
    def scrap_create(self,business,username,password,product_codes):
        self.normal(business,username,password)
        # try:
        self.click_acc(sLocation.stock_loss_add)
        self.click_acc(sLocation.product_type_edit)
        self.click_acc(sLocation.change_product)
        self.click_acc(sLocation.stock_type_edit)
        self.click_acc(sLocation.choose_stock_type)
        reason = "%s%s%s%s" % (chr(random.randint(65, 90)), chr(random.randint(97, 122)), chr(random.randint(97, 122)),
                      chr(random.randint(65, 90)))
        self.input_by_acc(sLocation.resean_edit,reason)
        time.sleep(2)
        self.click_acc(basePage.disappear_keyboard)
        self.click_acc(sLocation.stock_loss_next)
        time.sleep(5)
        h5_order.add_product(self,product_codes,'order')
        # except Exception as e:
        #     raise Exception('创建损益单时出现异常:%s'%e)

    # 提交出库
    def scrap_upload(self,business,username,password,product_codes):
        self.normal(business,username,password)
        # try:
        self.click_acc(sLocation.default_state)
        self.click_acc(sLocation.draft_order)
        has_submit = self.find_element(sLocation.submit)
        detail = self.find_element(basePage.table_len)
        if has_submit == False:
            self.click_acc(sLocation.stock_loss_add)
            self.click_acc(sLocation.product_type_edit)
            self.click_acc(sLocation.change_product)
            self.click_acc(sLocation.stock_type_edit)
            self.click_acc(sLocation.choose_stock_type)
            reason = "%s%s%s%s" % (
            chr(random.randint(65, 90)), chr(random.randint(97, 122)), chr(random.randint(97, 122)),
            chr(random.randint(65, 90)))
            self.input_by_acc(sLocation.resean_edit, reason)
            time.sleep(2)
            self.click_acc(basePage.disappear_keyboard)
            self.click_acc(sLocation.stock_loss_next)
            time.sleep(5)
            h5_order.add_product(self, product_codes, 'order')
            self.click_acc(sLocation.submit)
            self.click_acc(sLocation.submitok)
            time.sleep(5)
        elif detail == False:
            self.click_acc(basePage.details_text)
            time.sleep(5)
            h5_order.add_product(self, product_codes, 'order')
            time.sleep(3)
            self.click_acc(sLocation.submit)
            self.click_acc(sLocation.submitok)
            time.sleep(5)

        else:
            self.click_acc(sLocation.submit)
            self.click_acc(sLocation.submitok)
            time.sleep(5)
        # except Exception as e:
        #     raise Exception('提交损益出现异常%s'%e)


    def scrap_by_orderno(self, business, username, password):
        '''
        调拨入库单高级搜索,根据调拨单号进行模糊搜索
        :return:
        '''
        # try:
        self.normal(business, username, password)
        basePage.search_advanced_receipts(self, '1', 'inventory')
        # except Exception as e:
        #     raise Exception('损益单高级搜索出现异常:%s'%e)