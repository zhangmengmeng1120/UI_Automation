#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from ios_page_location import basePage
import time
from ios_page_location import transferOutLocation as tranLocation
from h5_pages import h5_order

class TransferOut(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    # 调拨出库单创建
    def transfer_out_create(self,business,username,password,product_codes):
        basePage.login(self,business,username,password)
        # try:
        self.click_acc(basePage.menu)
        time.sleep(4)
        # 点击门店出库
        self.click_acc(basePage.stock_out)
        # 点击调拨出库
        self.click_acc(basePage.transfer_out)
        self.click_acc(tranLocation.allocate_add)
        self.click_acc(tranLocation.shop_edit)
        self.click_element(tranLocation.choose_shop)
        self.click_acc(tranLocation.type_edit)
        self.click_acc(tranLocation.choose_type)
        self.click_acc(tranLocation.et_allocate_reason)
        self.click_acc(tranLocation.change_reason)
        self.click_acc(tranLocation.allocate_next)
        h5_order.add_product(self,product_codes,'order')
        # except Exception as e:
        #     raise Exception('创建调拨单时出现异常:%s'%e)

    # 提交出库
    def transfer_out_upload(self,business,username,password,product_codes):
        basePage.login(self,business,username,password)
        # try:
        self.click_acc(basePage.menu)
        time.sleep(4)
        # 点击门店出库
        self.click_acc(basePage.stock_out)
        # 点击调拨出库
        self.click_acc(basePage.transfer_out)
        self.click_acc(tranLocation.title)
        self.click_acc(tranLocation.draft_order)
        self.click_acc(tranLocation.confirm_allocate_txt)
        self.click_acc(tranLocation.confirm_tip)
        self.click_acc(tranLocation.allocate_next)
        self.click_acc(tranLocation.text_confirm)

        # except Exception as e:
        #     raise Exception('提交调拨出库出现异常%s'%e)


    def transferout_by_orderno(self, business, username, password):
        '''
        调拨入库单高级搜索,根据调拨单号进行模糊搜索
        :return:
        '''
        # 登录
        basePage.login(self, business, username, password)
        # try:
        # 点击菜单
        self.click_acc(basePage.menu)
        # 点击门店出库
        self.click_acc(basePage.stock_out)
        # 点击调拨出库
        self.click_acc(basePage.transfer_out)
        # 点击高级搜索
        basePage.search_advanced_receipts(self,'1','transfer_out')
        # except Exception as e:
        #     raise Exception('调拨出库单高级搜索出现异常:%s'%e)