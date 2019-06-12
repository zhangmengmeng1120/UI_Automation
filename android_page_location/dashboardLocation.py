#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By

# 数据罗盘button
module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'数据罗盘')]")

datepicker_wizard = (By.CLASS_NAME, 'wrapper')

type_day = (By.ID, 'dp-day')
type_week = (By.ID, 'dp-week')
type_month = (By.ID, 'dp-month')
type_range = (By.ID, 'dp-range')
# 选择日期
first_day = (By.XPATH, '//table[@class="month1"]/tbody/tr[1]/td[1]/div')

search_button = (By.XPATH, "//button[text()='查询']")

# ===================>>>>>>>门店销售<<<<<<<<===============================

shop_sale_button = (By.XPATH, "//a[text()='门店销售']")

# 销售统计  选择日期
sale_map_datepicker = (By.XPATH, '//*[@id="datepicker1"]')
# 员工销售统计  选择日期
employee_sale_datepicker = (By.XPATH, '//*[@id="datepicker2"]')
# 销售走势  选择日期
sale_trend_datepicker = (By.XPATH, '//*[@id="datepicker4"]')
# 时段分析   选择日期
peroid_analysis_datepicker = (By.XPATH, '//*[@id="datepicker3"]')

# ===================>>>>>>>门店指标<<<<<<<<===============================
shop_indicator_button = (By.XPATH, "//a[text()='门店指标']")

# 门店销售指标 查看更多详情
shop_indicator_moredwc_button = (By.XPATH, "//button[text()='查看更多详情']")
day_indicator_label = (By.XPATH, '//*[@id="main2"]/div/div[3]/div[1]/label[1]')
week_indicator_label = (By.XPATH, '//*[@id="main2"]/div/div[3]/div[1]/label[2]')
month_indicator_label = (By.XPATH, '//*[@id="main2"]/div/div[3]/div[1]/label[3]')

day_datetap = (By.XPATH, '//*[@id="main2"]/div/div[4]/div[2]/label[1]')
week_datetap = (By.XPATH, '//*[@id="main2"]/div/div[4]/div[2]/label[2]')
month_datetap = (By.XPATH, '//*[@id="main2"]/div/div[4]/div[2]/label[3]')

day_emp_indicator_datetap = (By.XPATH, '//*[@id="main2"]/div/div[6]/div[2]/label[1]')
week_emp_indicator_datetap = (By.XPATH, '//*[@id="main2"]/div/div[6]/div[2]/label[2]')
month_emp_indicator_datetap = (By.XPATH, '//*[@id="main2"]/div/div[6]/div[2]/label[3]')

# ===================>>>>>>>门店周报<<<<<<<<===============================
shop_weekly_button = (By.XPATH, "//a[text()='门店周报']")
shop_week_datepicker = (By.XPATH, '//*[@id="datepicker_week"]')

# 查看排名
rank_div = (By.XPATH, '//*[@id="big_block"]/div[2]/div[3]/div')
pk_button = (By.XPATH, "//button[text()='PK一下']")

# 活动商品
promotion_product_label = (By.XPATH, '//label[text()="活动商品"]')

# ===================>>>>>>>库存分析<<<<<<<<===============================

inventory_indicator_button = (By.XPATH, "//a[text()='库存分析']")
