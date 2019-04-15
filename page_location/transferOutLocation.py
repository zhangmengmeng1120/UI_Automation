#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By

# 门店出库button
stock_out = (By.XPATH, "//android.widget.TextView[contains(@text,'门店出库')]")
# 调拨出库button
transfer_out = (By.XPATH, "//android.widget.TextView[contains(@text,'调拨出库')]")
# 创建调拨出库单
allocate_add = (By.ID, 'com.nexttao.shopforce.test:id/allocate_add')
# 选择调入门店
shop_edit = (By.ID, 'com.nexttao.shopforce.test:id/shop_edit')
# 选择出库方式
type_edit = (By.ID, 'com.nexttao.shopforce.test:id/type_edit')
# 选择调拨原因
et_allocate_reason = (By.ID, 'com.nexttao.shopforce.test:id/et_allocate_reason')
# 下一步
allocate_next = (By.ID, 'com.nexttao.shopforce.test:id/allocate_next')

# 下拉选择调入门店
change_shop = (By.ID, 'com.nexttao.shopforce.test:id/name')
# 下拉选择出库方式
change_stock = (By.ID, 'com.nexttao.shopforce.test:id/reason')
# 下拉选择调拨原因
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