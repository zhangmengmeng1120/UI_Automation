#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from android_page_location import orderQueryLocation as oqLocation
from android_page_location import basePage
import time



class QuerySaleOrder(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def normal_info(self,business,username,password):
        basePage.login(self, business, username, password)
        try:
            # 点击菜单
            self.click_element(basePage.menu_btn_layout)
            # 点击查询订单
            self.click_element(oqLocation.module_item_name)
            assert self.find_element(oqLocation.scan_layout),'False'
        except Exception as e:
            raise Exception('进入查询订单页面出现异常%s'%e)


    # ===================>>>>>>>高级搜索，根据小票号<<<<<<<<===============================

    def search_by_orderno(self, business, username, password, order_no):
        '''
        下拉刷新，上拉加载，根据订单号模糊搜索订单
        :param business: 商户号
        :param username: 用户名
        :param password: 密码
        :param order_no: 订单号，用于高级搜索
        :return:
        '''

        # 登录
        self.normal_info(business, username, password)
        try:
            time.sleep(2)
            # 展开订单信息
            self.click_element(oqLocation.fold_image)
            # 下拉刷新
            basePage.swipe_up(self, basePage.GetPageSize(self), 0.1, 0.2, 0.1, 0.62)
            time.sleep(4)
            for i in range(3):
                # 上拉加载
                basePage.swipe_up(self, basePage.GetPageSize(self), 0.1, 0.75, 0.1, 0.25)
                time.sleep(1)
            basePage.search_advanced_receipts(self,order_no)
            basePage.log_out(self)
        except Exception as e:
            raise Exception('订单查询/小票号出现异常%s'%e)

    # ===================>>>>>>>高级搜索，sku<<<<<<<<===============================

    def search_by_sku(self, business, username, password, sku):
        '''
        下拉刷新，上拉加载，根据订单号模糊搜索订单
        :param business: 商户号
        :param username: 用户名
        :param password: 密码
        :param order_no: 订单号，用于高级搜索
        :return:
        '''

        # 登录
        self.normal_info(business, username, password)
        try:
            time.sleep(2)
            # 展开订单信息
            self.click_element(oqLocation.fold_image)
            # 下拉刷新
            basePage.swipe_up(self, basePage.GetPageSize(self), 0.1, 0.2, 0.1, 0.62)
            time.sleep(4)
            for i in range(3):
                # 上拉加载
                basePage.swipe_up(self, basePage.GetPageSize(self), 0.1, 0.75, 0.1, 0.25)
                time.sleep(1)
            basePage.search_advanced_sku(self, sku)
            basePage.log_out(self)
        except Exception as e:
            raise Exception('订单查询/sku出现异常%s' % e)


    # ===================>>>>>>>订单状态过滤<<<<<<<<===============================

    def filtrate_order(self, business, username, password):
        '''
        根据订单状态筛选订单
        '''
        # 登录
        self.normal_info(business, username, password)

        try:
            time.sleep(2)
            # 点击全部订单
            self.click_element(oqLocation.query_order_title)
            # 随机选择全部订单、普通订单、退货订单、换货订单
            self.click_element(oqLocation.order_of_state)
            if self.find_element(oqLocation.query_order_title).text == '退货订单':
                assert self.find_element(oqLocation.order_type).text,'退'
            elif self.find_element(oqLocation.query_order_title).text == '换货订单':
                if self.find_element(oqLocation.order_type).text == '换':
                    print '订单筛选正常'
                else:
                    raise Exception('订单筛选异常')
            self.click_element(basePage.menu_btn_layout)
            basePage.swipe_up(self, basePage.GetPageSize(self), 0.1, 0.75, 0.1, 0.25)
            self.click_element(basePage.logout)
            self.click_element(basePage.text_confirm)
        except Exception as e:
            raise Exception('查询订单高级搜索出现异常%s'%e)


