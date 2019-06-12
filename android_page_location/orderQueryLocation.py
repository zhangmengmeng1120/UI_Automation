#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random
import basePage

# ===================>>>>>>>查询订单页面元素<<<<<<<<===============================

# 查询订单button
module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'查询订单')]")

# 扫描订单编号
scan_layout = (By.ID, '%s:id/scan_layout'%basePage.package_name)

# 定位第一个销售订单的位置
order_list_item_layout = (By.ID, '%s:id/order_list_item_layout'%basePage.package_name)

# 展开订单信息
fold_image = (By.ID, '%s:id/fold_image'%basePage.package_name)

# 点击全部订单
query_order_title = (By.ID, '%s:id/query_order_title'%basePage.package_name)

# 订单状态
state_num = random.randint(1, 4)
order_of_state = (By.XPATH, "//android.widget.TextView[%s]" % state_num)

# 用于判断退换货订单
order_type = (By.ID, '%s:id/order_type'%basePage.package_name)
