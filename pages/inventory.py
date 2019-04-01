#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from selenium.webdriver.common.by import By
import basePage
from basePage import login
import time
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Inventory(BaseFunction):
    def __init__(self,driver):
        BaseFunction.__init__(self,driver)

    def inventory_create(self,business,username,password,rack_name):
        '''
        创建盘点单
        :return:
        '''
        # 门店盘点button
        self.module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'门店盘点')]")
        # 创建盘点button
        self.stock_list_add_btn = (By.ID, 'com.nexttao.shopforce.test:id/stock_list_add_btn')
        # 提交button
        self.new_inventory_submit_btn = (By.ID, 'com.nexttao.shopforce.test:id/new_inventory_submit_btn')
        # 添加货架
        self.add_rack = (By.XPATH, "//android.widget.TextView[contains(@text,'添加货架')]")
        # 输入货架名称
        self.input_text = (By.ID, 'com.nexttao.shopforce.test:id/input_text')
        # 确认
        self.text_confirm = (By.ID, 'com.nexttao.shopforce.test:id/text_confirm')

        login(business,username,password)

    def inventory_filtrate(self):
        '''
        根据盘点单状态筛选盘点单
        :return:
        '''
        # 门店盘点button
        self.module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'门店盘点')]")
        # 订单状态下拉
        self.title = (By.ID, 'com.nexttao.shopforce.test:id/title')
        # 订单状态
        state_num = random.randint(1, 5)
        self.order_of_state = (By.XPATH, "//android.widget.TextView[%s]" % state_num)
        # 明细
        self.shelves_list_operate = (By.ID, 'com.nexttao.shopforce.test:id/shelves_list_operate')
        # SKU
        self.shelves_details_sku_tab = (By.ID, 'com.nexttao.shopforce.test:id/shelves_details_sku_tab')
        # SPU
        self.shelves_details_spu_tab = (By.ID, 'com.nexttao.shopforce.test:id/shelves_details_spu_tab')
        # 搜索
        self.shelves_details_search = (By.ID, 'com.nexttao.shopforce.test:id/shelves_details_search')
        # 返回
        self.shelves_details_back = (By.ID, 'com.nexttao.shopforce.test:id/shelves_details_back')
        # 查看差异
        self.inventory_details_view_diff_btn = (By.ID, 'com.nexttao.shopforce.test:id/inventory_details_view_diff_btn')
        # 盘点红冲
        self.inventory_details_check_btn = (By.ID, 'com.nexttao.shopforce.test:id/inventory_details_check_btn')
        # 展开盘点信息
        self.expand_btn = (By.ID, 'com.nexttao.shopforce.test:id/expand_btn')





    def inventory_query(self):
        '''
        盘点单高级搜索
        :return:
        '''
        # 门店盘点button
        self.module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'门店盘点')]")
        # 高级搜索
        self.order_search = (By.ID, 'com.nexttao.shopforce.test:id/order_search')
        # 重置
        self.search_clear = (By.ID, 'com.nexttao.shopforce.test:id/search_clear')
        # 查询
        self.search_query = (By.ID, 'com.nexttao.shopforce.test:id/search_query')
        # 根据盘点单号进行搜索
        self.search_order_no = (By.ID, 'com.nexttao.shopforce.test:id/search_order_no')
        # 取消
        self.search_cancel = (By.ID, 'com.nexttao.shopforce.test:id/search_cancel')
