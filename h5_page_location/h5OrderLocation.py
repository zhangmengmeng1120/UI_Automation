#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random

# ===================>>>>>>>手工添加商品通用元素<<<<<<<<===============================

# 手工添加,在补货单中是第二个
add_handle = {'order':(By.XPATH, "//div[@class='before-focus']/div[1]"),'reload':(By.XPATH, "//div[@class='before-focus']/div[2]")}
# 选择商品颜色
product_colors = (By.XPATH, "//div[@class='sku-con']/div[1]/div[2]/div[1]")
# 选择商品尺码
product_size = (By.XPATH, "//div[@class='sku-con']/div[2]/div[2]/div[1]")
# 确认button
add = (By.CLASS_NAME, 'add')
# 返回
back_btn = (By.XPATH, "//div[@class='icon-back']/img[@alt='<']")
# 保存
btn_save = (By.CLASS_NAME, 'btn-save')
# 保存该页面的操作
confirm = (By.XPATH, "//div[@class='mint-msgbox']/div[3]/button[2]")
# 只看差异
btn_view_diff = (By.CLASS_NAME, 'btn-view-diff')
# 搜索button
searchIcon = (By.ID, 'searchIcon')
# 搜索条件
input_item = (By.CLASS_NAME, 'input-item')
# 清空搜索内容
icon_delete = (By.XPATH, "//div[@class='keyboard']/div[1]/img[@class='icon-delete']")
# 清空列表
btn_close_native = (By.CLASS_NAME, 'btn-close-native')
# 点击修改收货数量
icon_edit = (By.XPATH, "//table[@class='el-table__body']/tbody[1]/tr[1]/td[3]/div[1]/div[2]/div[2]")
# 填写收货数量
div_num = random.randint(1,9)
num_key = (By.XPATH, "//div[@class='keyboard']/div[2]/div[%s]"%div_num)
num_keys = (By.XPATH, "//div[@class='keyboard']/div[2]")
# 确认修改收货数量
key_confirm = (By.XPATH, "//div[@class='keyboard']/div[2]/div[12]")
# 订单内容
result_item = (By.CLASS_NAME, 'result-item')



# ===================>>>>>>>盘点商品详情<<<<<<<<===============================
# 搜索输入框
search_input = (By.CLASS_NAME, 'input-item')
# 搜索icon
search_icon = (By.CLASS_NAME, 'icon-search-blue')
# 补打小票
btn_print = (By.CLASS_NAME, 'btn-print')
# 盘点修正
inven_btn_save = (By.CLASS_NAME, 'btn-save')
# 下拉选择图标
el_input_suffix = (By.CLASS_NAME, 'el-input__suffix')
# SPU/款
spu_select = (By.CLASS_NAME, 'el-select-dropdown__item')
# 链接，差异数量
link_by_num = (By.XPATH, "//tr[@class='el-table__row'][2]/td[6]/div/span")
# 链接，差异金额
link_by_amount = (By.XPATH, "//tr[@class='el-table__row'][2]/td[7]/div/span")
# 关闭 商品变动明细页面
close_win = (By.XPATH, "//section[@class='filter2']/img")