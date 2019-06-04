#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from ios_page_location import basePage
from ios_page_location import deliveryReceiveLocation as deLocation
from h5_pages import h5_order
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class DeliveryReceive(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def delivery_confirm(self, business, username, password):
        '''
        签收待签收的单据
        :param business:
        :param username:
        :param password:
        :return:
        '''
        basePage.login(self, business, username, password)
        # try:
        # 点击菜单
        self.click_acc(basePage.menu)
        # 点击门店入库
        self.click_acc(basePage.stock_in)
        time.sleep(4)
        # 点击配货收货
        self.click_acc(basePage.delivery_receive)
        self.click_acc(deLocation.details_text)
        time.sleep(2)
        h5_order.confirm_product(self)
        self.click_acc(deLocation.take_receive)
        self.click_acc(deLocation.confirm)
        el = self.find_element_by_accessibility_id(deLocation.transfer_diff_wizard)
        if el:
            self.click_acc(deLocation.confirm_by_delivery)
        self.click_acc(deLocation.cancel)
        # except:
        #     raise Exception('签收配货收货单出现异常')


    def delivery_by_orderno(self, business, username, password,):
        '''
        调拨入库单高级搜索,根据调拨单号进行模糊搜索
        :return:
        '''
        # 登录
        basePage.login(self, business, username, password)
        # try:
        # 点击菜单
        self.click_acc(basePage.menu)
        # 点击门店入库
        self.click_acc(basePage.stock_in)
        time.sleep(3)
        # print self.driver.page_source

        # self.driver.execute_script("mobile:dragFromToForDuration",
        #                            {"duration": 5.0, "element": None, "fromX": 40.0, "fromY": 500.0, "toX": 40.0,
        #                             "toY": 130.0})
        # print self.driver.page_source
        # # # 点击调拨入库
        self.click_acc(basePage.delivery_receive)
        #
        basePage.search_advanced_receipts(self,'1','inventory')
        # except Exception as e:
        #     raise Exception('调拨入库单高级搜索出现异常:%s'%e)
