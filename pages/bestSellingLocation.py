#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By

# 畅销排行button
module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'畅销排行')]")
# 搜索button
search_product_btn = (By.ID, 'com.nexttao.shopforce.test:id/search_product_btn')