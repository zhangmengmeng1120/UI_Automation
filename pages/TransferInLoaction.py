#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random

# 门店入库button
stock_in = (By.XPATH, "//android.widget.TextView[contains(@text,'门店入库')]")
# 调拨入库button
transfer_in = (By.XPATH, "//android.widget.TextView[contains(@text,'调拨入库')]")
# 确认签收button
take_receive = (By.ID, 'com.nexttao.shopforce.test:id/take_receive')
# 查看详情
details_text = (By.ID, 'com.nexttao.shopforce.test:id/details_text')
# 填写收货数量，这是h5页面

# 订单状态
state_num = random.randint(1, 4)
order_of_state = (By.XPATH, "//android.widget.TextView[%s]" % state_num)
# 订单状态下拉
title = (By.ID, 'com.nexttao.shopforce.test:id/title')
# 展开订单详情
fold_image = (By.ID, 'com.nexttao.shopforce.test:id/fold_image')

# 高级搜索button
order_search = (By.ID, 'com.nexttao.shopforce.test:id/order_search')
# 查询
search_query = (By.ID, 'com.nexttao.shopforce.test:id/search_query')
# 调拨单号输入框
search_order_no = (By.ID, 'com.nexttao.shopforce.test:id/search_order_no')
# 商品编码输入框
search_order_sku = (By.ID, 'com.nexttao.shopforce.test:id/search_order_sku')
# 发货店仓输入框
search_order_org = (By.ID, 'com.nexttao.shopforce.test:id/search_order_org')
# 操作人输入框
operate_edit = (By.ID, 'com.nexttao.shopforce.test:id/operate_edit')
# 重置
search_clear = (By.ID, 'com.nexttao.shopforce.test:id/search_clear')
# 取消
search_up_cancel = (By.ID, 'com.nexttao.shopforce.test:id/search_up_cancel')
# 调拨单状态
order_state = (By.XPATH, "//android.widget.TextView[contains(@text,'已完成')]")
# 调拨单号
allocate_name = (By.ID, 'com.nexttao.shopforce.test:id/allocate_name')