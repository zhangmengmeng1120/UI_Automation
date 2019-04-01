#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By

# 会员中心button
menu_info = (By.XPATH, "//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[3]")
# 未绑定二维码会弹出提示信息
iterm = (By.XPATH, "//android.widget.TextView[contains(@text,'收银终端[POS-漂亮]未绑定二维码')]")
# 查看该会员是否已经存在要添加的标签
old_tag = (By.XPATH, "//android.widget.TextView[contains(@text,%s)]")
# 确认提示操作
text_confirm = (By.ID, 'com.nexttao.shopforce.test:id/text_confirm')
# 搜索button
search_product_btn = (By.ID, 'com.nexttao.shopforce.test:id/search_product_btn')
# 添加标签button
addTagBtn = (By.ID, 'com.nexttao.shopforce.test:id/addTagBtn')
# 自定义标签输入框
custom_targs = (By.ID, 'com.nexttao.shopforce.test:id/custom_targs')
# 确认添加标签button
add_targs_button = (By.ID, 'com.nexttao.shopforce.test:id/add_targs_button')
# 确定button
confirm_button = (By.ID, 'com.nexttao.shopforce.test:id/confirm_button')
# 验证标签是否添加成功
tags_text = (By.XPATH, "//android.widget.TextView[contains(@text,tag)]")
# 会员画像
radio_pic = (By.ID, 'com.nexttao.shopforce.test:id/radio_pic')
# 历史订单
radio_history = (By.ID, 'com.nexttao.shopforce.test:id/radio_history')
# 优惠券
coupon_layout = (By.ID, 'com.nexttao.shopforce.test:id/coupon_layout')
# 返回button
member_back = (By.ID, 'com.nexttao.shopforce.test:id/member_back')
# 注册会员
add_member_txt = (By.ID, 'com.nexttao.shopforce.test:id/add_member_txt')
# 提示信息
hint_text = (By.ID, 'com.nexttao.shopforce.test:id/hint_text')
# 会员姓名
register_name = (By.ID, 'com.nexttao.shopforce.test:id/register_name')
# 会员性别
sex = [(By.ID, 'com.nexttao.shopforce.test:id/checkman'),
       (By.ID, 'com.nexttao.shopforce.test:id/checkwomen')]
# 注册button
register_save = (By.ID, 'com.nexttao.shopforce.test:id/register_save')
# 确认注册
tag_info = (By.XPATH, "//android.widget.TextView[contains(@text,'%s')]")
# 改会员改单button
sale_btn = (By.ID, 'com.nexttao.shopforce.test:id/sale_btn')
# 验证是否将会员信息带到购物车页面
member_name = (By.ID, 'com.nexttao.shopforce.test:id/member_name')
