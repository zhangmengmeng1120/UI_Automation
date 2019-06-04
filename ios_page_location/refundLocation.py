#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
from android_pages import basePage

# ===================>>>>>>>调拨出库单页面<<<<<<<<===============================
# 创建调拨出库单
allocate_add = '新建单据'
# 查看明细
details_text = '查看明细'
# 订单状态
title = '默认状态'
# 草稿状态的订单
draft_order = '草稿'
# 待签收的订单
confirm_order = '待签收'
# 取消调拨单
cancel_btn = '取消退货'
# 提交出库
confirm_allocate_txt = '出库'
# 提示信息，出库日期
confirm_tip = '确定'
# 出库确认
text_confirm = '出库确认'


# ===================>>>>>>>创建调拨出库单<<<<<<<<===============================

# 选择调入门店
shop_edit = '请选择目标门店'
# 选择调拨原因
et_allocate_reason = '请选择退货原因'
# 选中调入门店
choose_shop= (By.XPATH,'//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText')
# 下拉选择退货原因
change_reason = '物品损坏'
# 下一步，出库确认
allocate_next = '下一步'
# 退出
exit_create = '退出'


