#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random

# ===================>>>>>>>损益单页面元素<<<<<<<<===============================

# 创建损益单
stock_loss_add = '新建单据'
# 提交
submit = '提交'
# 确定
submitok = '确定'
# 全部状态
default_state = '默认状态'
# 草稿
draft_order = '草稿'




# ===================>>>>>>>损益单创建页面元素<<<<<<<<===============================
# 物品类型
product_type_edit = '物品类型'
change_product = random.choice(['商品','辅料'])
# 损益类型
stock_type_edit = '损溢类型'
choose_stock_type = random.choice(['货物丢失','货物破损','其它损耗'])
# 损益原因
resean_edit =  '损溢原因最多可输入255个字'
# 下一步
stock_loss_next = '下一步'
