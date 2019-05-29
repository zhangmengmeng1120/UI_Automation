#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random
from android_pages import basePage
# 门店盘点button
module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'门店盘点')]")
# 检查是否存在盘点中的单子
inventory_details_cancel_btn = (By.ID, '%s:id/inventory_details_cancel_btn'%basePage.package_name)
# 创建盘点button
stock_list_add_btn = (By.ID, '%s:id/stock_list_add_btn'%basePage.package_name)
# 提交button
new_inventory_submit_btn = (By.ID, '%s:id/new_inventory_submit_btn'%basePage.package_name)
# 添加货架
add_rack = (By.XPATH, "//android.widget.TextView[contains(@text,'添加货架')]")
# 输入货架名称
rack_name = (By.ID, '%s:id/input_text'%basePage.package_name)
# 确认
text_confirm = (By.ID, '%s:id/text_confirm'%basePage.package_name)
# 订单状态下拉
title = (By.ID, '%s:id/title'%basePage.package_name)
# 订单状态
state_num = random.randint(1, 5)
order_of_state = (By.XPATH, "//android.widget.TextView[%s]" % state_num)
# 明细
shelves_list_operate = (By.ID, '%s:id/shelves_list_operate'%basePage.package_name)
# SKU
shelves_details_sku_tab = (By.ID, '%s:id/shelves_details_sku_tab'%basePage.package_name)
# SPU
shelves_details_spu_tab = (By.ID, '%s:id/shelves_details_spu_tab'%basePage.package_name)
# 搜索
shelves_details_search = (By.ID, '%s:id/shelves_details_search'%basePage.package_name)
# 返回
shelves_details_back = (By.ID, '%s:id/shelves_details_back'%basePage.package_name)
# 查看差异
inventory_details_view_diff_btn = (By.ID, '%s:id/inventory_details_view_diff_btn'%basePage.package_name)
# 盘点红冲
inventory_details_check_btn = (By.ID, '%s:id/inventory_details_check_btn'%basePage.package_name)
# 展开盘点信息
expand_btn = (By.ID, '%s:id/expand_btn'%basePage.package_name)
# 高级搜索
order_search = (By.ID, '%s:id/order_search'%basePage.package_name)
# 重置
search_clear = (By.ID, '%s:id/search_clear'%basePage.package_name)
# 查询
search_query = (By.ID, '%s:id/search_query'%basePage.package_name)
# 根据盘点单号进行搜索
search_order_no = (By.ID, '%s:id/search_order_no'%basePage.package_name)
# 取消
search_cancel = (By.ID, '%s:id/search_cancel'%basePage.package_name)