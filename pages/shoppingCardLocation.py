#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By

# 商品搜索
keypad_search_btn = (By.ID, 'com.nexttao.shopforce.test:id/keypad_search_btn')
# 商品尺码
product_sizes = [(By.XPATH,"//android.widget.TextView[contains(@text,'M')]"),(By.XPATH,"//android.widget.TextView[contains(@text,'L')]"),(By.XPATH,"//android.widget.TextView[contains(@text,'XL')]")]
# 商品颜色
product_colors = [(By.XPATH, "//android.widget.TextView[contains(@text,'黑色')]")]
# 添加商品
confirm_txt = (By.ID, 'com.nexttao.shopforce.test:id/confirm_txt')
# 清空购物车
shopcar_clear_btn = (By.ID, 'com.nexttao.shopforce.test:id/shopcar_clear_btn')
# 确认清空购物车，确认提示信息
text_confirm = (By.ID, 'com.nexttao.shopforce.test:id/text_confirm')
# 销售员
saleman_text = (By.ID, 'com.nexttao.shopforce.test:id/saleman_text')
# 第一个销售员的id
tv_sale_name = (By.ID, 'com.nexttao.shopforce.test:id/tv_sale_name')
# 确认选中的销售员
tv_confirm = (By.ID, 'com.nexttao.shopforce.test:id/tv_confirm')
# 购物车页面下一步button，去支付button
settle_btn = (By.ID, 'com.nexttao.shopforce.test:id/settle_btn')
# 用于判断是否进入购物车页面
member_promotion_name = (By.ID, 'com.nexttao.shopforce.test:id/member_promotion_name')
# 支付方式
pay_cash = (By.XPATH, "//android.widget.TextView[contains(@text,'现金')]")
# 确认支付
confirm_pay = (By.ID, 'com.nexttao.shopforce.test:id/confirm_pay')
# 用来判断是否支付完成
img_gou = (By.ID, 'com.nexttao.shopforce.test:id/img_gou')
# 开始新订单
text_restart = (By.ID, 'com.nexttao.shopforce.test:id/text_restart')