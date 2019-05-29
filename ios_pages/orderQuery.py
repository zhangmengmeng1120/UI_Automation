#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from ios_page_location import orderQueryLocaton as oqLocation
from ios_page_location.basePage import login
from ios_page_location import basePage
from android_pages.basePage import swipe_up,GetPageSize
import time

class QuerySaleOrder(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    # ===================>>>>>>>高级搜索，根据小票号<<<<<<<<===============================
    def search_order_info(self, merchantID, username, password, order_no):
        '''
        下拉刷新，上拉加载，根据订单号模糊搜索订单
        :param merchantID: 商户号
        :param username: 用户名
        :param password: 密码
        :param order_no: 订单号，用于高级搜索
        :return:
        '''
        try:
            # 登录
            login(self, merchantID, username, password)
            time.sleep(8)
            receipts_type = 'sale_order'
            # 点击菜单
            self.click_acc(basePage.menu)
            self.click_acc(oqLocation.order_query_button)
            basePage.search_advanced_receipts(self,order_no,receipts_type)
            time.sleep(1)
        except Exception as e:
            raise Exception('订单查询出现异常%s'%e)

    # ===================>>>>>>>高级搜索，根据sku<<<<<<<<===============================

    def search_order_by_sku(self, merchantID, username, password, sku_info):

        login(self, merchantID, username, password)
        time.sleep(8)
        # 点击菜单
        self.click_acc(basePage.menu)
        self.click_acc(oqLocation.order_query_button)
        basePage.search_advanced_sku(self,sku_info)
        time.sleep(2)

    # ===================>>>>>>>订单状态过滤<<<<<<<<===============================

    def filter_order_state(self, merchantID, username, password):

        login(self, merchantID, username, password)
        time.sleep(8)
        # 点击菜单
        self.click_acc(basePage.menu)
        self.click_acc(oqLocation.order_query_button)
        self.click_acc(oqLocation.all_orders)
        time.sleep(1)
        self.click_acc(oqLocation.order_normal)
        time.sleep(1)
        self.click_acc(oqLocation.order_refund)
        time.sleep(1)
        self.click_acc(oqLocation.order_exchange)
        time.sleep(1)