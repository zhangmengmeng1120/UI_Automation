#!/usr/bin/python
# encoding:utf-8
import unittest
import time
from android_pages.shoppingCard import SalePage
from android_pages.orderQuery import QuerySaleOrder
from android_pages.memberCenter import MemberCenter
from android_pages.transferIn import TransferIn
from android_pages.bestSelling import BestSelling
from android_pages.report import Report
from android_pages.transferOut import TransferOut
from android_pages.refund import Refund
from android_pages.scrap import Scrap
from android_pages.deliveryReceive import DeliveryReceive
from android_pages.dashboard import Dashboard
from android_pages.cloudOrder import CloudOrder
from android_pages.reload import Reload
from base_appium_function.init_driver import init_driver
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


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
        self.product_codes = ['1821012', '1721001']

    def shop_card(self):
        test_info = SalePage(self.driver)
        test_info.sale_test(self.business, self.username, self.password, self.product_code, self.telphone)

    def select_orderno(self):
        test_info = QuerySaleOrder(self.driver)
        test_info.search_by_orderno(self.business, self.username, self.password, self.order_no)

    def select_order_sku(self):
        test_info = QuerySaleOrder(self.driver)
        test_info.search_by_sku(self.business, self.username, self.password, self.product_code)

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
        test_info = BestSelling(self.driver)
        test_info.best_info(self.business, self.username, self.password, self.product_code)

    def shop_inventory(self):
        test_info = Report(self.driver)
        test_info.shop_inventory(self.business, self.username, self.password)

    def shop_inventory_diff(self):
        test_info = Report(self.driver)
        test_info.shop_inventory_diff(self.business, self.username, self.password)

    def basic_report_act(self):
        test_info = Report(self.driver)
        test_info.basic_report_act(self.business, self.username, self.password)

    def transferout_create(self):
        test_info = TransferOut(self.driver)
        test_info.transfer_out_create(self.business, self.username, self.password, self.product_codes)

    def transferout_upload(self):
        test_info = TransferOut(self.driver)
        test_info.transfer_out_upload(self.business, self.username, self.password, self.product_codes)

    def transferout_search(self):
        test_info = TransferOut(self.driver)
        test_info.transferout_by_orderno(self.business, self.username, self.password, self.transferin_order,
                                         self.product_code)

    def refundCreate(self):
        test_info = Refund(self.driver)
        test_info.refund_create(self.business, self.username, self.password, self.product_codes)

    def refundUpload(self):
        test_info = Refund(self.driver)
        test_info.refund_upload(self.business, self.username, self.password, self.product_codes)

    def refund_search(self):
        test_info = Refund(self.driver)
        test_info.refund_by_orderno(self.business, self.username, self.password, self.transferin_order,
                                    self.product_code)

    def scrapCreate(self):
        test_info = Scrap(self.driver)
        test_info.scrap_create(self.business, self.username, self.password, self.product_codes)

    def scrapUpload(self):
        test_info = Scrap(self.driver)
        test_info.scrap_upload(self.business, self.username, self.password, self.product_codes)

    def scrap_search(self):
        test_info = Scrap(self.driver)
        test_info.scrap_by_orderno(self.business, self.username, self.password, self.transferin_order,
                                   self.product_code)

    def delivery_receive(self):
        test_info = DeliveryReceive(self.driver)
        test_info.delivery_confirm(self.business, self.username, self.password)

    def basic_dashboard_act(self):
        test_info = Dashboard(self.driver)
        test_info.basic_dashboard_act(self.business, self.username, self.password)

    def basic_cloud_act(self):
        test_info = CloudOrder(self.driver)
        test_info.basic_cloud_act(self.business, self.username, self.password, self.product_code)

    def basic_reload_act(self):
        test_info = Reload(self.driver)
        test_info.basic_reload_act(self.business, self.username, self.password, self.product_codes)

    # 释放实例，释放资源
    def tearDown(self):
        self.driver.quit()
