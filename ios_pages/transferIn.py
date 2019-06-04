#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from ios_page_location import basePage
from ios_page_location import transferInLocation as tranLocation
from h5_pages import h5_order
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class TransferIn(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def transfer_confirm(self, business, username, password,product_codes):
        '''
        签收待签收的单据
        :param business:
        :param username:
        :param password:
        :return:
        '''
        basePage.login(self, business, username, password)
        try:
            # 点击菜单
            self.click_acc(basePage.menu)
            # 点击门店入库
            self.click_acc(basePage.stock_in)
            # 点击调拨入库
            self.click_acc(basePage.transfer_in)
            el = self.find_element_by_accessibility_id(tranLocation.take_receive)
            if el:
                self.click_acc(tranLocation.details_text)
                time.sleep(4)
                h5_order.confirm_product(self)
                time.sleep(2)
                self.click_acc(tranLocation.take_receive)
                self.click_acc(tranLocation.confirm)
                diff = self.find_element(tranLocation.transfer_diff_wizard)
                if diff:
                    self.click_acc(tranLocation.confirm_by_delivery)
                self.click_acc(tranLocation.confirm_ok)
        except:
            raise Exception('签收调拨单出现异常')

    def transfer_by_orderno(self, business, username, password,product_code):
        '''
        调拨入库单高级搜索,根据调拨单号进行模糊搜索
        :return:
        '''
        # 登录
        basePage.login(self, business, username, password)
        try:
            # 点击菜单
            self.click_acc(basePage.menu)
            # 点击门店入库
            self.click_acc(basePage.stock_in)
            # 点击调拨入库
            self.click_acc(basePage.transfer_in)
            basePage.search_advanced_receipts(self,1,'transfer_in')
        except Exception as e:
            raise Exception('调拨入库单高级搜索出现异常:%s'%e)
