#!/usr/bin/python
# encoding:utf-8
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
from android_pages.shoppingCard import SalePage
from ios_pages.orderQuery import QuerySaleOrder
from ios_pages.memberCenter import MemberCenter
from ios_pages.transferIn import TransferIn
from ios_pages.bestSelling import BestSelling
from ios_pages.report import Report
from ios_pages.transferOut import TransferOut
from ios_pages.refund import Refund
from ios_pages.scrap import Scrap
from ios_pages.deliveryReceive import DeliveryReceive
from ios_pages.dashboard import Dashboard
from ios_pages.cloudOrder import CloudOrder
from ios_pages.reload import Reload
from ios_pages.inventory import StockInventory

from base_appium_function.ios_init_driver import init_driver
import random


class info(unittest.TestCase):
    def setUp(self):
        self.driver = init_driver()
        self.business = 'crm_test'
        self.username = 'pl'
        self.password = '123'
        self.product_code = '1821012'
        self.telphone = '13511831143'
        self.order_no = '5098'
        self.tags = '%s%s%s%s' % (
            chr(random.randint(65, 90)), chr(random.randint(97, 122)), chr(random.randint(97, 122)),
            chr(random.randint(65, 90)))
        self.rack_name = '%s%s%s%s' % (
            chr(random.randint(65, 90)), chr(random.randint(97, 122)), chr(random.randint(97, 122)),
            chr(random.randint(65, 90)))
        self.transferin_order = '1'
        self.product_codes = ['1821012', '1721001']

    # def shop_card(self):
    #     test_info = SalePage(self.driver)
    #     test_info.sale_test(self.business, self.username, self.password, self.product_code, self.telphone)
    #     time.sleep(10)

    # ===================>>>>>>>查询订单case<<<<<<<<===============================

    def select_order(self):
        test_info = QuerySaleOrder(self.driver)
        test_info.search_order_info(self.business, self.username, self.password, self.order_no)

    def select_order_sku(self):
        test_info = QuerySaleOrder(self.driver)
        test_info.search_order_by_sku(self.business, self.username, self.password, self.product_code)

    def filter_order(self):
        test_info = QuerySaleOrder(self.driver)
        test_info.filter_order_state(self.business, self.username, self.password)

    # ===================>>>>>>>会员中心case<<<<<<<<===============================

    def member_registers(self):
        test_info = MemberCenter(self.driver)
        test_info.member_register(self.business, self.username, self.password)
    def member_center(self):
        test_info = MemberCenter(self.driver)
        test_info.member_query(self.business, self.username, self.password, self.telphone)

    # ===================>>>>>>>调拨入库case<<<<<<<<===============================

    # 调拨入库高级搜索
    def transfer_search(self):
        test_info = TransferIn(self.driver)
        test_info.transfer_by_orderno(self.business, self.username, self.password, self.transferin_order)

    # 调拨入库确认签收
    def transfer_confirm(self):
        test_info = TransferIn(self.driver)
        test_info.transfer_confirm(self.business, self.username, self.password,self.product_codes)


    # ===================>>>>>>>畅销排行case<<<<<<<<===============================
    def bestsell(self):
        test_info = BestSelling(self.driver)
        test_info.best_info(self.business, self.username, self.password, self.product_code)
    #

    # ===================>>>>>>>查询报表case<<<<<<<<===============================

    def shop_inventory(self):
        test_info = Report(self.driver)
        test_info.shop_inventory(self.business, self.username, self.password)

    def shop_inventory_diff(self):
        test_info = Report(self.driver)
        test_info.shop_inventory_diff(self.business, self.username, self.password)

    def basic_report_act(self):
        test_info = Report(self.driver)
        test_info.basic_report_act(self.business, self.username, self.password)

    # ===================>>>>>>>调拨出库case<<<<<<<<===============================
    #
    def transferout_create(self):
        test_info = TransferOut(self.driver)
        test_info.transfer_out_create(self.business, self.username, self.password, self.product_codes)
    #
    def transferout_upload(self):
        test_info = TransferOut(self.driver)
        test_info.transfer_out_upload(self.business, self.username, self.password, self.product_codes)
    #
    def transferout_search(self):
        test_info = TransferOut(self.driver)
        test_info.transferout_by_orderno(self.business, self.username, self.password)

    # ===================>>>>>>>配货退货case<<<<<<<<===============================

    def refundCreate(self):
        test_info = Refund(self.driver)
        test_info.refund_create(self.business, self.username, self.password, self.product_codes)

    def refundUpload(self):
        test_info = Refund(self.driver)
        test_info.refund_upload(self.business, self.username, self.password, self.product_codes)

    def refund_search(self):
        test_info = Refund(self.driver)
        test_info.refund_by_orderno(self.business, self.username, self.password)

    # ===================>>>>>>>损益单case<<<<<<<<===============================
    def scrapCreate(self):
        test_info = Scrap(self.driver)
        test_info.scrap_create(self.business, self.username, self.password, self.product_codes)

    def scrapUpload(self):
        test_info = Scrap(self.driver)
        test_info.scrap_upload(self.business, self.username, self.password, self.product_codes)

    def scrap_search(self):
        test_info = Scrap(self.driver)
        test_info.scrap_by_orderno(self.business, self.username, self.password)

    # ===================>>>>>>>配货收货case<<<<<<<<===============================
    # 签收
    def delivery_receive(self):
        test_info = DeliveryReceive(self.driver)
        test_info.delivery_confirm(self.business, self.username, self.password)

    # 高级搜索
    def delivery_receive_advanced(self):
        test_info = DeliveryReceive(self.driver)
        test_info.delivery_by_orderno(self.business, self.username, self.password)

    # ===================>>>>>>>dashboard case<<<<<<<<===============================
    def basic_dashboard_act(self):
        test_info = Dashboard(self.driver)
        test_info.basic_dashboard_act(self.business, self.username, self.password)

    # ===================>>>>>>>云仓订单case<<<<<<<<===============================

    def basic_cloud_act(self):
        test_info = CloudOrder(self.driver)
        test_info.basic_cloud_act(self.business, self.username, self.password, self.product_code)

    # ===================>>>>>>>补货单case<<<<<<<<===============================
    def apply_reload_act(self):
        test_info = Reload(self.driver)
        test_info.apply_reload(self.business, self.username, self.password, self.product_codes)

    def approve_reload_act(self):
        test_info = Reload(self.driver)
        test_info.approve_reload(self.business, self.username, self.password)

    # ===================>>>>>>>盘点case<<<<<<<<===============================
    def inventory_stock_create(self):
        test_info = StockInventory(self.driver)
        test_info.inventory_create(self.business, self.username, self.password,self.product_codes)

    def inventory_stock_query(self):
        test_info = StockInventory(self.driver)
        test_info.inventory_query(self.business, self.username, self.password)

    def inventory_detail_diff(self):
        test_info = StockInventory(self.driver)
        test_info.inventory_read_diff(self.business, self.username, self.password,self.product_code)

    # 释放实例，释放资源
    def tearDown(self):
        self.driver.quit()
