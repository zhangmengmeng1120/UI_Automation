#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
from pages import basePage


# 会员中心button
menu_info = (By.XPATH, "//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[3]")
# 未绑定二维码会弹出提示信息
iterm = (By.XPATH, "//android.widget.TextView[contains(@text,'收银终端[POS-漂亮]未绑定二维码')]")
# 查看该会员是否已经存在要添加的标签
old_tag = (By.XPATH, "//android.widget.TextView[contains(@text,%s)]")
# 确认提示操作
text_confirm = (By.ID, '%s:id/text_confirm'%basePage.package_name)
# 搜索button
search_product_btn = (By.ID, '%s:id/search_product_btn'%basePage.package_name)
# 添加标签button
addTagBtn = (By.ID, '%s:id/addTagBtn'%basePage.package_name)
# 自定义标签输入框
custom_targs = (By.ID, '%s:id/custom_targs'%basePage.package_name)
# 确认添加标签button
add_targs_button = (By.ID, '%s:id/add_targs_button'%basePage.package_name)
# 确定button
confirm_button = (By.ID, '%s:id/confirm_button'%basePage.package_name)
# 验证标签是否添加成功
tags_text = (By.XPATH, "//android.widget.TextView[contains(@text,tag)]")
# 会员画像
radio_pic = (By.ID, '%s:id/radio_pic'%basePage.package_name)
# 历史订单
radio_history = (By.ID, '%s:id/radio_history'%basePage.package_name)
# 优惠券
coupon_layout = (By.ID, '%s:id/coupon_layout'%basePage.package_name)
# 返回button
member_back = (By.ID, '%s:id/member_back'%basePage.package_name)
# 注册会员
add_member_txt = (By.ID, '%s:id/add_member_txt'%basePage.package_name)
# 提示信息
hint_text = (By.ID, '%s:id/hint_text'%basePage.package_name)
# 会员姓名
register_name = (By.ID, '%s:id/register_name'%basePage.package_name)
# 会员性别
sex = [(By.ID, '%s:id/checkman'%basePage.package_name),
       (By.ID, '%s:id/checkwomen'%basePage.package_name)]
# 注册button
register_save = (By.ID, '%s:id/register_save'%basePage.package_name)
# 确认注册
tag_info = (By.XPATH, "//android.widget.TextView[contains(@text,'%s')]")
# 改会员改单button
sale_btn = (By.ID, '%s:id/sale_btn'%basePage.package_name)
# 验证是否将会员信息带到购物车页面
member_name = (By.ID, '%s:id/member_name'%basePage.package_name)
