#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
from pages import basePage

# 补货订单
module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'补货订单')]")

# ===================>>>>>>>补货申请<<<<<<<<===============================
reload_apply_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'补货申请')]")

# 状态选择
reload_state_choice = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[4]/div[2]')

# 草稿
draft_reload = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[3]/div[2]/div[2]')
# 待审批
approve_reload = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[3]/div[2]/div[3]')
# 待收货
waiting_reload = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[3]/div[2]/div[4]')
# 已完成
done_reload = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[3]/div[2]/div[5]')
# 已拒绝
reject_reload = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[3]/div[2]/div[6]')
# 已取消
cancel_reload = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[3]/div[2]/div[7]')

# 提交申请
cancel_reload_button = (By.CLASS_NAME, 'reject_btn')
commit_reload_button = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[3]/div[2]')

conform_commit = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]')
cancel_commit = (By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')

# 新增补货申请
add_new_reload = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[4]/div[3]')
# 门店发货
shop_transfer_button = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]')

choose_shop = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div')

first_shop = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]')
# 下一步
next_step = (By.XPATH, '//*[@id="app"]/div/div[3]/div[3]')

# 手工添加商品
add_product = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[2]')

search_product = (By.ID, '%s:id/search_product' % basePage.package_name)

add_handle = (By.XPATH, "//div[@class='before-focus']/div[1]")
# 选择商品颜色
product_colors = (By.XPATH, "//div[@class='sku-con']/div[1]/div[2]/div[1]")
# 选择商品尺码
product_size = (By.XPATH, "//div[@class='sku-con']/div[2]/div[2]/div[1]")
# 确认button
add = (By.CLASS_NAME, 'add')
# 返回
back_btn = (By.XPATH, "//div[@class='icon-back']/img[@alt='<']")
# 保存该页面的操作
confirm = (By.XPATH, "//div[@class='mint-msgbox']/div[3]/button[2]")

# ===================>>>>>>>补货审批<<<<<<<<===============================
reload_approve_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'补货审批')]")
