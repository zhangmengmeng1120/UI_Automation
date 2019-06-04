#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By


# ===================>>>>>>>补货申请页面元素<<<<<<<<===============================

# 全部状态
reload_state_choice = '全部状态'
# 草稿
draft_reload = '草稿'
# 待审批
approve_reload = '待审批'
# 待收货
waiting_reload = '待收货'
# 已完成
done_reload = '已完成'
# 已拒绝
reject_reload = '已拒绝'
# 已取消
cancel_reload = '已取消'
# 取消申请
cancel_reload_button = '取消申请'
# 提交申请
commit_reload_button = '提交申请'
# 新增补货申请
add_new_reload = '新建单据'

# ===================>>>>>>>补货申请单新建页面元素<<<<<<<<===============================
# 请选择发货店仓
stock_default = '请选择发货店仓'
# 选择第一个仓库
choose_stock = (By.XPATH,'//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]')
# 下一步
next_step = '下一步'
# 确认取消补货申请单
cancel_ok = '确认'


# ===================>>>>>>>补货审批页面元素<<<<<<<<===============================

# 待发货
waiting_delivery = '待发货'
# 同意发货
agree_delivery = '同意发货'
# 发货
delivery = '发货'