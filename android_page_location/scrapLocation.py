#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
from android_pages import basePage

# 损益单button
scrap = (By.XPATH, "//android.widget.TextView[contains(@text,'库存损溢')]")
# 创建损益单
stock_loss_add = (By.ID, '%s:id/stock_loss_add'%basePage.package_name)
# 请选择物品类型
product_type_edit = (By.ID, '%s:id/product_type_edit'%basePage.package_name)
# 请选择损益类型
stock_type_edit = (By.ID, '%s:id/stock_type_edit'%basePage.package_name)
# 下一步
stock_loss_next = (By.ID, '%s:id/stock_loss_next'%basePage.package_name)
# 确认出库
allocate_next = (By.ID, '%s:id/allocate_next'%basePage.package_name)
# 发货
send_btn = (By.ID, '%s:id/send_btn'%basePage.package_name)

# 下拉选择武平类型
change_product = (By.XPATH, "//android.widget.TextView[contains(@text,'商品')]")
# 下拉选择损益类型
change_reason = (By.ID, '%s:id/reason'%basePage.package_name)
# 损益原因
resean_edit = (By.ID, '%s:id/resean_edit'%basePage.package_name)

# 取消损益
cancel_btn = (By.ID, '%s:id/cancel_btn'%basePage.package_name)
# 提交损益
confirm_stock_loss_txt = (By.ID, '%s:id/confirm_stock_loss_txt'%basePage.package_name)
# 查看详情
details_text = (By.ID, '%s:id/details_text'%basePage.package_name)
# 提示信息，明细行不能为空
confirm_tip = (By.XPATH, "//android.widget.TextView[contains(@text,'明细行不能为空')]")
# 明细行不能为空点击确定
text_confirm = (By.ID, '%s:id/text_confirm'%basePage.package_name)

# H5页面
# 手工添加
add_handle = (By.XPATH, "//div[@class='before-focus']/div[1]")
search_product = (By.ID, '%s:id/search_product'%basePage.package_name)
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
title = (By.ID, '%s:id/stock_loss_title'%basePage.package_name)
# 草稿状态的订单
draft_order = (By.XPATH, "//android.widget.TextView[contains(@text,'草稿')]")

# 高级搜索button
order_search = (By.ID, '%s:id/order_search'%basePage.package_name)
# 查询
search_query = (By.ID, '%s:id/search_query'%basePage.package_name)
# 退货单号输入框
search_order_no = (By.ID, '%s:id/search_order_no'%basePage.package_name)
# 商品编码输入框
search_order_sku = (By.ID, '%s:id/search_order_sku'%basePage.package_name)
# 发货店仓输入框
search_order_org = (By.ID, '%s:id/search_order_org'%basePage.package_name)

# 日期范围
all_check = (By.ID, '%s:id/all_check'%basePage.package_name)
out_check = (By.ID, '%s:id/out_check'%basePage.package_name)
in_check = (By.ID, '%s:id/in_check'%basePage.package_name)
# 操作人输入框
operate_edit = (By.ID, '%s:id/operate_edit'%basePage.package_name)
# 重置
search_clear = (By.ID, '%s:id/search_clear'%basePage.package_name)
# 取消
search_up_cancel = (By.ID, '%s:id/search_up_cancel'%basePage.package_name)
