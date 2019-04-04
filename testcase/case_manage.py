#!/usr/bin/python
# encoding:utf-8
import unittest
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import time
from  pages.shoppingCard import SalePage
from pages.orderQuery import QuerySaleOrder
from pages.memberCenterPage import MemberCenter
from pages.TransferIn import TransferIn
from pages.bestSelling import BestSelling
from base_appium_function.init_driver import init_driver
import random


class info(unittest.TestCase):
    def setUp(self):
        self.driver = init_driver()
        self.business = 'crm_test'
        self.username = 'pl'
        self.password = '123'
        self.product_code = '1821012'
        self.telphone = '13511831143'
        self.order_no = '2365'
        self.tags = '%s%s%s%s' % (
            chr(random.randint(65, 90)), chr(random.randint(97, 122)), chr(random.randint(97, 122)),
            chr(random.randint(65, 90)))
        self.rack_name = '%s%s%s%s' % (
            chr(random.randint(65, 90)), chr(random.randint(97, 122)), chr(random.randint(97, 122)),
            chr(random.randint(65, 90)))
        self.transferin_order = '1'

    def shop_card(self):
        test_info = SalePage(self.driver)
        test_info.sale_test(self.business, self.username, self.password, self.product_code, self.telphone)
        time.sleep(10)

    def select_order(self):
        test_info = QuerySaleOrder(self.driver)
        test_info.search_order_info(self.business, self.username, self.password, self.order_no)
        time.sleep(10)

    def filtrate_order(self):
        test_info = QuerySaleOrder(self.driver)
        test_info.filtrate_order(self.business, self.username, self.password)

    def member_registers(self):
        test_info = MemberCenter(self.driver)
        test_info.member_register(self.business, self.username, self.password, self.tags)

    def member_center(self):
        test_info = MemberCenter(self.driver)
        test_info.member_query(self.business, self.username, self.password, self.telphone, self.tags)

    # 调拨入库高级搜索
    def transfer_search(self):
        test_info = TransferIn(self.driver)
        test_info.transfer_by_orderno(self.business, self.username, self.password, self.transferin_order,
                                      self.product_code)

    # 调拨入库确认签收
    def transfer_confirm(self):
        test_info = TransferIn(self.driver)
        test_info.transfer_confirm(self.business, self.username, self.password)

    def bestsell(self):
        test_info =BestSelling(self.driver)
        test_info.best_info(self.business, self.username, self.password)
    # 释放实例，释放资源
    def tearDown(self):
        self.driver.quit()
