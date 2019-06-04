#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from ios_page_location import basePage
import time
from ios_page_location import refundLocation as reLocation
from h5_pages import h5_order

class Refund(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    # 配货退货单创建
    def refund_create(self,business,username,password,product_codes):
        basePage.login(self,business,username,password)
        # try:
        self.click_acc(basePage.menu)
        time.sleep(4)
        # 点击门店出库
        self.click_acc(basePage.stock_out)
        # 点击调拨出库
        self.click_acc(basePage.refund)
        self.click_acc(reLocation.allocate_add)
        self.click_acc(reLocation.shop_edit)
        self.click_element(reLocation.choose_shop)
        self.click_acc(reLocation.et_allocate_reason)
        self.click_acc(reLocation.change_reason)
        self.click_acc(reLocation.allocate_next)
        time.sleep(2)
        h5_order.add_product(self,product_codes,'order')
        # except Exception as e:
        #     raise Exception('创建调拨单时出现异常:%s'%e)

    # 提交出库
    def refund_upload(self,business,username,password,product_codes):
        basePage.login(self,business,username,password)
        # try:
        self.click_acc(basePage.menu)
        time.sleep(4)
        # 点击门店出库
        self.click_acc(basePage.stock_out)
        # 点击调拨出库
        self.click_acc(basePage.refund)
        self.click_acc(reLocation.title)
        self.click_acc(reLocation.draft_order)
        self.click_acc(reLocation.confirm_allocate_txt)
        self.click_acc(reLocation.confirm_tip)
        self.click_acc(reLocation.text_confirm)

        # except Exception as e:
        #     raise Exception('提交调拨出库出现异常%s'%e)


    def refund_by_orderno(self, business, username, password):
        '''
        调拨入库单高级搜索,根据调拨单号进行模糊搜索
        :return:
        '''
        # 登录
        basePage.login(self, business, username, password)
        # try:
        # 点击菜单
        self.click_acc(basePage.menu)
        time.sleep(4)
        # 点击门店出库
        self.click_acc(basePage.stock_out)
        # 点击调拨出库
        self.click_acc(basePage.refund)
        # 点击高级搜索
        basePage.search_advanced_receipts(self,'1','inventory')
        # except Exception as e:
        #     raise Exception('调拨出库单高级搜索出现异常:%s'%e)