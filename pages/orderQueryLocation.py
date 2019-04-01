#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random

# 查询订单button
module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'查询订单')]")
# 扫描订单编号
scan_layout = (By.ID, 'com.nexttao.shopforce.test:id/scan_layout')
# 定位第一个销售订单的位置
order_list_item_layout = (By.ID, 'com.nexttao.shopforce.test:id/order_list_item_layout')
# 高级搜索页面
order_search = (By.ID, 'com.nexttao.shopforce.test:id/order_search')
# 小票输入框
search_order_no = (By.ID, 'com.nexttao.shopforce.test:id/search_order_no')
# 搜索button
search_query = (By.ID, 'com.nexttao.shopforce.test:id/search_query')
# 重置button
search_clear = (By.ID, 'com.nexttao.shopforce.test:id/search_clear')
# 展开订单信息
fold_image = (By.ID, 'com.nexttao.shopforce.test:id/fold_image')
# 点击全部订单
query_order_title = (By.ID, 'com.nexttao.shopforce.test:id/query_order_title')
# 订单状态
state_num = random.randint(1,4)
order_of_state = (By.XPATH, "//android.widget.TextView[%s]"%state_num)
# 退货订单状态的上一级id
num = random.randint(1,10)
refund_order = (By.XPATH, "//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[%s]/android.widget.LinearLayout[1]/android.widget.TextView[2]"%num)
exchange_order = (By.XPATH, "//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[%s]/android.widget.LinearLayout[1]/android.widget.TextView[2]"%num)