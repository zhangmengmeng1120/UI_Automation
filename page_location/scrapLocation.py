#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By

# 损益单button
scrap = (By.XPATH, "//android.widget.TextView[contains(@text,'库存损溢')]")
# 创建损益单
stock_loss_add = (By.ID, 'com.nexttao.shopforce.test:id/stock_loss_add')
# 请选择物品类型
product_type_edit = (By.ID, 'com.nexttao.shopforce.test:id/product_type_edit')
# 请选择损益类型
stock_type_edit = (By.ID, 'com.nexttao.shopforce.test:id/stock_type_edit')
# 下一步
stock_loss_next = (By.ID, 'com.nexttao.shopforce.test:id/stock_loss_next')
# 确认出库
allocate_next = (By.ID, 'com.nexttao.shopforce.test:id/allocate_next')
# 发货
send_btn = (By.ID, 'com.nexttao.shopforce.test:id/send_btn')

# 下拉选择武平类型
change_product = (By.XPATH, "//android.widget.TextView[contains(@text,'商品')]")
# 下拉选择损益类型
change_reason = (By.ID, 'com.nexttao.shopforce.test:id/reason')
# 损益原因
resean_edit = (By.ID, 'com.nexttao.shopforce.test:id/resean_edit')

# 取消损益
cancel_btn = (By.ID, 'com.nexttao.shopforce.test:id/cancel_btn')
# 提交损益
confirm_stock_loss_txt = (By.ID, 'com.nexttao.shopforce.test:id/confirm_stock_loss_txt')
# 查看详情
details_text = (By.ID, 'com.nexttao.shopforce.test:id/details_text')
# 提示信息，明细行不能为空
confirm_tip = (By.XPATH, "//android.widget.TextView[contains(@text,'明细行不能为空')]")
# 明细行不能为空点击确定
text_confirm = (By.ID, 'com.nexttao.shopforce.test:id/text_confirm')

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
title = (By.ID, 'com.nexttao.shopforce.test:id/stock_loss_title')
# 草稿状态的订单
draft_order = (By.XPATH, "//android.widget.TextView[contains(@text,'草稿')]")

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
