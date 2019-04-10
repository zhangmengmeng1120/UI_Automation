#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random

# 畅销排行button
module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'畅销排行')]")
# 搜索button
search_product_btn = (By.ID, 'com.nexttao.shopforce.test:id/search_product_btn')
# 随机获取排行前8的商品
num = random.randint(1, 8)
favourite_product = (By.XPATH,
                     "//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[2]/android.view.View[%s]" % num)
back_btn = (By.XPATH,
            "//android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]")
# 搜索框
search_edit_text = (By.XPATH,
                    "//android.webkit.WebView[@content-desc=\"畅销排行\"]/android.view.View[1]/android.view.View[1]/android.widget.EditText")
# 商品详情
pronduct_detail = (By.XPATH,
                   "//android.view.View[@content-desc=\"商品详情\"]")
# 搜索结果
searcg_product = (By.XPATH,
                  "//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[1]")
# 更新产品或促销进度条
update_text_info = (By.ID, 'com.nexttao.shopforce.test:id/update_text_info')
