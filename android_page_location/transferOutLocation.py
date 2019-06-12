#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import basePage

# 门店出库button
stock_out = (By.XPATH, "//android.widget.TextView[contains(@text,'门店出库')]")
# 调拨出库button
transfer_out = (By.XPATH, "//android.widget.TextView[contains(@text,'调拨出库')]")
# 创建调拨出库单
allocate_add = (By.ID, '%s:id/allocate_add'%basePage.package_name)
# 选择调入门店
shop_edit = (By.ID, '%s:id/shop_edit'%basePage.package_name)
# 选择出库方式
type_edit = (By.ID, '%s:id/type_edit'%basePage.package_name)
# 选择调拨原因
et_allocate_reason = (By.ID, '%s:id/et_allocate_reason'%basePage.package_name)
# 下一步，出库确认
allocate_next = (By.ID, '%s:id/allocate_next'%basePage.package_name)

# 下拉选择调入门店
change_shop = (By.ID, '%s:id/name'%basePage.package_name)
# 下拉选择出库方式
change_stock = (By.ID, '%s:id/reason'%basePage.package_name)
# 下拉选择调拨原因
change_reason = (By.ID, '%s:id/reason'%basePage.package_name)

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
title = (By.ID, '%s:id/title'%basePage.package_name)
# 草稿状态的订单
draft_order = (By.XPATH, "//android.widget.TextView[contains(@text,'草稿')]")
# 获取草稿订单出库数量
transfer_num = (By.XPATH, "//android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[5]")
# 获取调拨单是否有被红冲
out_bound = (By.XPATH, "//android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]")
# 取消调拨单
cancel_btn = (By.ID, '%s:id/cancel_btn'%basePage.package_name)
# 提交出库
confirm_allocate_txt = (By.ID, '%s:id/confirm_allocate_txt'%basePage.package_name)
# 提示信息，出库数量不能全为0
confirm_tip = (By.XPATH, "//android.widget.TextView[contains(@text,'出库数量不能全为0')]")
# 出库数量不能为0的提示，以及确认取消调拨单
text_confirm = (By.ID, '%s:id/text_confirm'%basePage.package_name)
# 调拨红冲
allocate_txt = (By.ID, '%s:id/allocate_txt'%basePage.package_name)
# 待签收调拨单
confirm_order = (By.XPATH, "//android.widget.TextView[contains(@text,'待签收')]")
# 查看详情
details_text = (By.ID, '%s:id/details_text'%basePage.package_name)
# 高级搜索button
order_search = (By.ID, '%s:id/order_search'%basePage.package_name)
# 查询
search_query = (By.ID, '%s:id/search_query'%basePage.package_name)
# 调拨单号输入框
search_order_no = (By.ID, '%s:id/search_order_no'%basePage.package_name)
# 商品编码输入框
search_order_sku = (By.ID, '%s:id/search_order_sku'%basePage.package_name)
# 收货店仓输入框
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
