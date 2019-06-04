#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By

# ===================>>>>>>>盘点页面<<<<<<<<===============================

# 门店盘点
menu_info = '门店盘点'
# 左
left = '左'
# 明细
detail = '明细'
# 删除货架
del_goods_shelves = '删除货架'
# 编辑
edit = '编 辑'
# 新建单据
add_btn = '新建单据'
# 添加货架
add_goods_shelves = '盘点－添加货架'
# 提交盘点
submit = '提交盘点'
# 查看盘点差异
inven_diff = '查看盘点差异'
# 取消盘点
inven_cancel = '取消盘点'


# ===================>>>>>>>新建盘点页面<<<<<<<<===============================

# 提交
add = '提交'
# 取消
add_cancel = '取消'

# ===================>>>>>>>新建货架<<<<<<<<===============================

# 货架名称
rack_name = (By.XPATH, '//XCUIElementTypeTextField[@value="请输入货架名称"]')
# 商品库位
stock_name = (By.XPATH, '//XCUIElementTypeTextField[@value="请选择商品库位"]')
# 选择库位
stock_type = '可售'
# 确定
rack_confirm = '确定'
# 取消
rack_cancel= '取消'

# ===================>>>>>>>盘点明细<<<<<<<<===============================

# 点击商品的sku进入商品明细变动
detail_sku = (By.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText')