#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random

# ===================>>>>>>>会员中心页面<<<<<<<<===============================

# 会员中心
menu_info = '会员中心'
# 搜索会员
search_member = '搜 索 会 员'
# 注册会员
register_member = '注 册 会 员'
# 会员详情页面返回键
back_btn = '页面返回键'

# ===================>>>>>>>会员画像页面<<<<<<<<===============================

# 会员画像
radio_pic = (By.XPATH, '//XCUIElementTypeStaticText[@name="会员画像"]')
# 该会员开单
member_sale_btn = '该会员开单'
# 消费行为
consumer_behavior = '消费行为'
# 会员标签
member_tag = '会员标签'
# 添加标签button
addTagBtn = '添加标签 '
# 确定
confirm = '确定'
# 取消
cancel = '取消'
# 标签设置
memberTagSettingIcon = 'memberTagSettingIcon'
# 清空
clear_all = '清空'
# 取消
cancel_setting = (By.XPATH, '//XCUIElementTypeButton[@name="取消"])[1]')
# 随机添加一个标签
tags = (By.XPATH, '//XCUIElementTypeApplication[@name="互道盈力Beta"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[%s]/XCUIElementTypeOther/XCUIElementTypeStaticText'%random.randint(1,6))


# ===================>>>>>>>会员资料页面<<<<<<<<===============================

# 会员资料
message = (By.XPATH, '//XCUIElementTypeStaticText[@name="会员资料"]')
# 会员资料list(包括姓名，卡号，性别，邮箱等信息)
memeber_info_list = (By.XPATH, '//XCUIElementTypeTable[@type="XCUIElementTypeTable"][2]')
# 会员邮箱
mail = (By.XPATH, '//XCUIElementTypeTextField[@value="请输入会员邮箱"]')
# 注册，会员姓名
member_name = (By.XPATH, '//XCUIElementTypeTextField[@value="请输入会员姓名"]')
# 会员性别
sex = (By.NAME, '//XCUIElementTypeButton[@value=""]')
# 保存信息
save_info = '保存信息'
# 确认注册
register_confirm = '确认注册'
#

# ===================>>>>>>>历史订单页面<<<<<<<<===============================

# 历史订单
radio_history = (By.XPATH, '//XCUIElementTypeStaticText[@name="历史订单"]')

# ===================>>>>>>>优惠券页面<<<<<<<<===============================

# 优惠券
coupon_layout = 'couponsUnselected'

