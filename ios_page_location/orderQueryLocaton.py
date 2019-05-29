#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By

# ===================>>>>>>>查询订单页面<<<<<<<<===============================

# 查询订单
order_query_button = '查询订单'
# 删除
delete_order = (By.XPATH,'//XCUIElementTypeButton[@name="删除"]')
# 继续
continue_order = (By.XPATH,'//XCUIElementTypeButton[@name="继续"]')
# 展开，查看订单更多信息
show_detail = 'PNG LeftMenuShowPushDown'

# ===================>>>>>>>订单状态页面<<<<<<<<===============================

# 全部订单
all_orders = '全部订单'
# 普通订单
order_normal = '普通订单'
# 退货订单
order_refund = '退货订单'
# 换货订单
order_exchange = '换货订单'




