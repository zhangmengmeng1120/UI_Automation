#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import basePage

# 商品尺码
product_sizes = [(By.XPATH, "//android.widget.TextView[contains(@text,'M')]"),
                 (By.XPATH, "//android.widget.TextView[contains(@text,'L')]"),
                 (By.XPATH, "//android.widget.TextView[contains(@text,'XL')]")]
# 商品颜色
product_colors = [(By.XPATH, "//android.widget.TextView[contains(@text,'黑色')]")]
# 添加商品
confirm_txt = (By.ID, '%s:id/confirm_txt'%basePage.package_name)
# 清空购物车
shopcar_clear_btn = (By.ID, '%s:id/shopcar_clear_btn'%basePage.package_name)
# 确认清空购物车，确认提示信息
text_confirm = (By.ID, '%s:id/text_confirm'%basePage.package_name)
# 销售员
saleman_text = (By.ID, '%s:id/saleman_text'%basePage.package_name)
# 第一个销售员的id
tv_sale_name = (By.ID, '%s:id/tv_sale_name'%basePage.package_name)
# 确认选中的销售员
tv_confirm = (By.ID, '%s:id/tv_confirm'%basePage.package_name)
# 购物车页面下一步button，去支付button
settle_btn = (By.ID, '%s:id/settle_btn'%basePage.package_name)
# 用于判断是否进入购物车页面
member_promotion_name = (By.ID, '%s:id/member_promotion_name'%basePage.package_name)
# 支付方式
pay_cash = (By.XPATH, "//android.widget.TextView[contains(@text,'现金')]")
# 确认支付
confirm_pay = (By.ID, '%s:id/confirm_pay'%basePage.package_name)
# 用来判断是否支付完成
img_gou = (By.ID, '%s:id/img_gou'%basePage.package_name)
# 开始新订单
text_restart = (By.ID, '%s:id/text_restart'%basePage.package_name)
