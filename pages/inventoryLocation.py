#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random
# 门店盘点button
module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'门店盘点')]")
# 创建盘点button
stock_list_add_btn = (By.ID, 'com.nexttao.shopforce.test:id/stock_list_add_btn')
# 提交button
new_inventory_submit_btn = (By.ID, 'com.nexttao.shopforce.test:id/new_inventory_submit_btn')
# 添加货架
add_rack = (By.XPATH, "//android.widget.TextView[contains(@text,'添加货架')]")
# 输入货架名称
input_text = (By.ID, 'com.nexttao.shopforce.test:id/input_text')
# 确认
text_confirm = (By.ID, 'com.nexttao.shopforce.test:id/text_confirm')
# 订单状态下拉
title = (By.ID, 'com.nexttao.shopforce.test:id/title')
# 订单状态
state_num = random.randint(1, 5)
order_of_state = (By.XPATH, "//android.widget.TextView[%s]" % state_num)
# 明细
shelves_list_operate = (By.ID, 'com.nexttao.shopforce.test:id/shelves_list_operate')
# SKU
shelves_details_sku_tab = (By.ID, 'com.nexttao.shopforce.test:id/shelves_details_sku_tab')
# SPU
shelves_details_spu_tab = (By.ID, 'com.nexttao.shopforce.test:id/shelves_details_spu_tab')
# 搜索
shelves_details_search = (By.ID, 'com.nexttao.shopforce.test:id/shelves_details_search')
# 返回
shelves_details_back = (By.ID, 'com.nexttao.shopforce.test:id/shelves_details_back')
# 查看差异
inventory_details_view_diff_btn = (By.ID, 'com.nexttao.shopforce.test:id/inventory_details_view_diff_btn')
# 盘点红冲
inventory_details_check_btn = (By.ID, 'com.nexttao.shopforce.test:id/inventory_details_check_btn')
# 展开盘点信息
expand_btn = (By.ID, 'com.nexttao.shopforce.test:id/expand_btn')
# 高级搜索
order_search = (By.ID, 'com.nexttao.shopforce.test:id/order_search')
# 重置
search_clear = (By.ID, 'com.nexttao.shopforce.test:id/search_clear')
# 查询
search_query = (By.ID, 'com.nexttao.shopforce.test:id/search_query')
# 根据盘点单号进行搜索
search_order_no = (By.ID, 'com.nexttao.shopforce.test:id/search_order_no')
# 取消
search_cancel = (By.ID, 'com.nexttao.shopforce.test:id/search_cancel')