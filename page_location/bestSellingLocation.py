#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By

# 畅销排行button
module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'畅销排行')]")
# 搜索button
search_product_btn = (By.CLASS_NAME, 'search_icon')
# 输入商品编码
input_product = (By.NAME, 'product_sku')
# 点击搜索
search = (By.CLASS_NAME, 'search')
# 取消搜索
cancel = (By.CLASS_NAME, 'cancel')
# 清空搜索消息
clear = (By.CLASS_NAME, 'del')
# 随机获取排行前8的商品
favourite_product = (By.XPATH, "//article/a[1]")
# 返回
back_btn = (By.XPATH, "//img[@src='assets/imgs/backs.png']")
# 同城库存
inventory = (By.XPATH, "//div[@class='tab']/a[2]")

