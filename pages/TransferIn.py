#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from basePage import login, swipe_up, GetPageSize
import basePage
import TransferInLoaction as Tlocation
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TransferIn(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def transfer_confirm(self, business, username, password):
        '''
        签收待签收的单据，高级搜索
        :param business:
        :param username:
        :param password:
        :return:
        '''
        login(self, business, username, password)
        time.sleep(5)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
        # 向上滑到页面
        page_size = GetPageSize(self)
        sx = 0.1
        sy = 0.75
        ex = 0.1
        ey = 0.25
        swipe_up(self, page_size, sx, sy, ex, ey)

        # 点击门店入库
        self.click_element(Tlocation.stock_in)
        # 点击调拨入库
        self.click_element(Tlocation.transfer_in)
        time.sleep(5)
        self.click_element(Tlocation.transfer_confirm_button)
        time.sleep(3)
        el = self.find_element(Tlocation.transfer_diff_wizard)
        if el:
            self.click_element(Tlocation.diff_confirm_button)
            time.sleep(3)
        self.click_element(Tlocation.text_confirm_button)

    def transfer_filtrate(self):
        return True

    def transfer_by_orderno(self, business, username, password, transferin_order, sku):
        '''
        调拨入库单高级搜索,根据调拨单号进行模糊搜索
        :return:
        '''
        # 登录
        login(self, business, username, password)
        time.sleep(5)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
        # 向上滑到页面
        page_size = GetPageSize(self)
        sx = 0.1
        sy = 0.75
        ex = 0.1
        ey = 0.25
        swipe_up(self, page_size, sx, sy, ex, ey)
        # 点击门店入库
        self.click_element(Tlocation.stock_in)
        # 点击调拨入库
        self.click_element(Tlocation.transfer_in)
        time.sleep(10)
        # 点击高级搜索
        self.click_element(Tlocation.order_search)
        # 输入调拨单号
        self.input_element(Tlocation.search_order_no, transferin_order)
        # 输入商品编码
        self.input_element(Tlocation.search_order_sku, sku)
        # 点击调拨类型
        self.click_element(Tlocation.type_edit)
        page_size = GetPageSize(self)
        sx = 0.5
        sy = 0.75
        ex = 0.5
        ey = 0.80
        swipe_up(self, page_size, sx, sy, ex, ey)
        time.sleep(5)
        self.click_element(Tlocation.transfer_options_submit)

        # 点击查询
        self.click_element(Tlocation.search_query)
        # el = self.find_element(Tlocation.order_state)
        # if el:
        #     if transferin_order in self.find_element(
        #             Tlocation.allocate_name).text:
        #         print '验证成功'
        # else:
        #     raise Exception('查找元素Tlocation.order_state的结果为%s' % el)

        self.click_element(basePage.menu_btn_layout)

        swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
        self.click_element(basePage.logout)
        self.click_element(basePage.text_confirm)
