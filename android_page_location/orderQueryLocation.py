#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random
from android_pages import basePage

# 查询订单button
module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'查询订单')]")
# 扫描订单编号
scan_layout = (By.ID, '%s:id/scan_layout'%basePage.package_name)
# 定位第一个销售订单的位置
order_list_item_layout = (By.ID, '%s:id/order_list_item_layout'%basePage.package_name)
# 高级搜索页面
order_search = (By.ID, '%s:id/order_search'%basePage.package_name)
# 小票输入框
search_order_no = (By.ID, '%s:id/search_order_no'%basePage.package_name)
# 搜索button
search_query = (By.ID, '%s:id/search_query'%basePage.package_name)
# 重置button
search_clear = (By.ID, '%s:id/search_clear'%basePage.package_name)
# 展开订单信息
fold_image = (By.ID, '%s:id/fold_image'%basePage.package_name)
# 点击全部订单
query_order_title = (By.ID, '%s:id/query_order_title'%basePage.package_name)
# 订单状态
state_num = random.randint(1, 4)
order_of_state = (By.XPATH, "//android.widget.TextView[%s]" % state_num)
# 退货订单状态的上一级id
num = random.randint(1, 10)
refund_order = (By.XPATH,
                "//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[%s]/android.widget.LinearLayout[1]/android.widget.TextView[2]" % num)
exchange_order = (By.XPATH,
                  "//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[%s]/android.widget.LinearLayout[1]/android.widget.TextView[2]" % num)
