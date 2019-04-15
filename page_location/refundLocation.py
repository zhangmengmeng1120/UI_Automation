#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By

# 门店出库button
stock_out = (By.XPATH, "//android.widget.TextView[contains(@text,'门店出库')]")
# 配货退货button
refund = (By.XPATH, "//android.widget.TextView[contains(@text,'配货退货')]")
# 创建配货退货单
allocate_add = (By.ID, 'com.nexttao.shopforce.test:id/allocate_add')
# 选择收货店仓
store_in_name = (By.ID, 'com.nexttao.shopforce.test:id/store_in_name')
# 选择退货原因
store_reason = (By.ID, 'com.nexttao.shopforce.test:id/store_reason')
# 下一步
stock_confirm = (By.ID, 'com.nexttao.shopforce.test:id/stock_confirm')
# 确认出库
allocate_next = (By.ID, 'com.nexttao.shopforce.test:id/allocate_next')
# 发货
send_btn = (By.ID, 'com.nexttao.shopforce.test:id/send_btn')

# 下拉选择调入门店
change_shop = (By.ID, 'com.nexttao.shopforce.test:id/tv_shop_name')
# 下拉选择退货原因
change_reason = (By.ID, 'com.nexttao.shopforce.test:id/reason')

# H5页面
# 手工添加
add_handle = (By.XPATH, "//div[@class='before-focus']/div[1]")
search_product = (By.ID, 'com.nexttao.shopforce.test:id/search_product')
# 选择商品颜色
product_colors = (By.XPATH, "//div[@class='sku-con']/div[1]/div[2]/div[1]")
# 选择商品尺码
product_size = (By.XPATH, "//div[@class='sku-con']/div[2]/div[2]/div[1]")
# 确认button
add = (By.CLASS_NAME, 'add')
# 返回
back_btn = (By.XPATH, "//div[@class='icon-back']/img[@alt='<']")
# 保存
btn_save = (By.CLASS_NAME, 'btn-save')
# 保存该页面的操作
confirm = (By.XPATH, "//div[@class='mint-msgbox']/div[3]/button[2]")

# 订单状态
title = (By.ID, 'com.nexttao.shopforce.test:id/title')
# 草稿状态的订单
draft_order = (By.XPATH, "//android.widget.TextView[contains(@text,'草稿')]")
# 默认状态的订单
waiting_order = (By.XPATH, "//android.widget.TextView[contains(@text,'待审批')]")
# 获取草稿订单出库数量
transfer_num = (By.XPATH, "//android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[5]")
# 取消配货退货单
cancel_btn = (By.ID, 'com.nexttao.shopforce.test:id/cancel_btn')
# 提交出库
confirm_return_txt = (By.ID, 'com.nexttao.shopforce.test:id/confirm_return_txt')
# 提示信息，出库数量不能全为0
confirm_tip = (By.XPATH, "//android.widget.TextView[contains(@text,'请先添加商品')]")
# 出库数量不能为0的提示，以及确认取消调拨单
text_confirm = (By.ID, 'com.nexttao.shopforce.test:id/text_confirm')
# 待签收配货退货单
confirm_order = (By.XPATH, "//android.widget.TextView[contains(@text,'待签收')]")
# 查看详情
details_text = (By.ID, 'com.nexttao.shopforce.test:id/details_text')
# 高级搜索button
order_search = (By.ID, 'com.nexttao.shopforce.test:id/order_search')
# 查询
search_query = (By.ID, 'com.nexttao.shopforce.test:id/search_query')
# 退货单号输入框
search_order_no = (By.ID, 'com.nexttao.shopforce.test:id/search_order_no')
# 商品编码输入框
search_order_sku = (By.ID, 'com.nexttao.shopforce.test:id/search_order_sku')
# 发货店仓输入框
search_order_org = (By.ID, 'com.nexttao.shopforce.test:id/search_order_org')

# 日期范围
all_check = (By.ID, 'com.nexttao.shopforce.test:id/all_check')
out_check = (By.ID, 'com.nexttao.shopforce.test:id/out_check')
in_check = (By.ID, 'com.nexttao.shopforce.test:id/in_check')
# 操作人输入框
operate_edit = (By.ID, 'com.nexttao.shopforce.test:id/operate_edit')
# 重置
search_clear = (By.ID, 'com.nexttao.shopforce.test:id/search_clear')
# 取消
search_up_cancel = (By.ID, 'com.nexttao.shopforce.test:id/search_up_cancel')
