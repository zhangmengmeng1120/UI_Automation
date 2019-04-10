#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
import orderQueryLocation as oqLocation
import basePage
import time
from basePage import login, GetPageSize, swipe_up


class QuerySaleOrder(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def search_order_info(self, business, username, password, order_no):
        '''
        下拉刷新，上拉加载，根据订单号模糊搜索订单
        :param business: 商户号
        :param username: 用户名
        :param password: 密码
        :param order_no: 订单号，用于高级搜索
        :return:
        '''

        # 登录
        login(self, business, username, password)
        time.sleep(3)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
        # 点击查询订单
        self.click_element(oqLocation.module_item_name)
        try:
            self.find_element(oqLocation.scan_layout)
        except:
            raise Exception('进入查询订单页面出现异常')
        time.sleep(10)
        # 展开订单信息
        self.click_element(oqLocation.fold_image)
        downs_x = 0.1
        downs_y = 0.2
        downe_x = 0.1
        downe_y = 0.62
        # 下拉刷新
        swipe_up(self, GetPageSize(self), downs_x, downs_y, downe_x, downe_y)
        time.sleep(10)
        s_x = 0.1
        s_y = 0.75
        e_x = 0.1
        e_y = 0.25
        for i in range(3):
            # 上拉加载
            swipe_up(self, GetPageSize(self), s_x, s_y, e_x, e_y)
            time.sleep(3)
        # 点击高级搜索
        self.click_element(oqLocation.order_search)
        # 输入搜索内容，小票号
        self.input_element(oqLocation.search_order_no, order_no)
        # 清空搜索内容
        self.click_element(oqLocation.search_clear)
        if self.find_element(oqLocation.search_order_no).text == '请输入销售订单号':
            print '内容清空完成'
        # 输入搜索内容，小票号
        self.input_element(oqLocation.search_order_no, order_no)
        # 点击搜索
        self.click_element(oqLocation.search_query)
        time.sleep(3)
        # 退出搜索
        downs_x = 0.1
        downs_y = 0.2
        downe_x = 0.1
        downe_y = 0.62
        swipe_up(self, GetPageSize(self), downs_x, downs_y, downe_x, downe_y)
        self.click_element(basePage.menu_btn_layout)
        sx = 0.1
        sy = 0.75
        ex = 0.1
        ey = 0.25
        swipe_up(self, GetPageSize(self), sx, sy, ex, ey)
        self.click_element(basePage.logout)
        self.click_element(basePage.text_confirm)

    def filtrate_order(self, business, username, password):
        '''
        根据订单状态筛选订单
        '''
        # 登录
        login(self, business, username, password)
        time.sleep(3)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
        # 点击查询订单
        self.click_element(oqLocation.module_item_name)
        try:
            self.find_element(oqLocation.scan_layout)
        except:
            raise Exception('进入查询订单页面出现异常')
        time.sleep(5)
        # 点击全部订单
        self.click_element(oqLocation.query_order_title)
        # 随机选择全部订单、普通订单、退货订单、换货订单
        self.click_element(oqLocation.order_of_state)
        if self.find_element(oqLocation.query_order_title).text == '退货订单':
            if self.find_element(oqLocation.refund_order).text == '退':
                print '订单筛选正常'
            else:
                raise Exception('订单筛选异常')
        elif self.find_element(oqLocation.query_order_title).text == '换货订单':
            if self.find_element(oqLocation.exchange_order).text == '换':
                print '订单筛选正常'
            else:
                raise Exception('订单筛选异常')
        self.click_element(basePage.menu_btn_layout)
        sx = 0.1
        sy = 0.75
        ex = 0.1
        ey = 0.25
        swipe_up(self, GetPageSize(self), sx, sy, ex, ey)
        self.click_element(basePage.logout)
        self.click_element(basePage.text_confirm)


