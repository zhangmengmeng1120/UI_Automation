#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random

# 查询报表button
module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'查询报表')]")

# 查询按钮
report_search_button = (By.XPATH, "//button[text()='查询']")

menu_back_button = (By.CLASS_NAME, "menuBack")

# ===================>>>>>>>库存查询<<<<<<<<===============================
# 门店库存
shop_inventory_button = (By.XPATH, "//span[text()='门店库存']")
# 门店库存（含差异）
shop_inventory_diff_button = (By.XPATH, "//span[text()='门店库存(含差异)']")

# ===================>>>>>>>零售查询<<<<<<<<===============================
# 商品排行
product_sale_rank_button = (By.XPATH, "//span[text()='商品排行']")
# 销售库存
sale_inventory_button = (By.XPATH, "//span[text()='销售库存']")
# 销售环比
sale_chain_rate_button = (By.XPATH, "//span[text()='销售环比']")
# 销售统计
sale_statistics_button = (By.XPATH, "//span[text()='销售统计']")
# 销售日报
sale_report_button = (By.XPATH, "//span[text()='销售日报']")

# ===================>>>>>>>员工查询<<<<<<<<===============================
# 销售分析
employee_sale_status_button = (By.XPATH, "//span[text()='销售分析']")
# ===================>>>>>>>业务单据<<<<<<<<===============================
# 业务单据
operation_receipts_button = (By.XPATH, "//div[1]/div[@class='md_zi']/span[text()='业务单据']")
# 店面进销存
delivery_inventory_button = (By.XPATH, "//span[text()='店面进销存']")
# 商品变动明细
product_move_button = (By.XPATH, "//span[text()='商品变动明细']")

# ===================>>>>>>>其他报表<<<<<<<<===============================
# 商场折扣统计
cut_payment_button = (By.XPATH, "//span[text()='商场折扣统计']")
# 付款方式查销售
payment_type_button = (By.XPATH, "//span[text()='付款方式查销售']")
# 在线支付
payment_records_button = (By.XPATH, "//span[text()='在线支付']")
# 促销查询
promotion_info_button = (By.XPATH, "//span[text()='促销查询']")

all_reports = [shop_inventory_button, shop_inventory_diff_button, product_sale_rank_button, sale_inventory_button,
               sale_chain_rate_button, sale_statistics_button, sale_report_button, employee_sale_status_button,
               operation_receipts_button, delivery_inventory_button, product_move_button, cut_payment_button,
               payment_type_button, payment_records_button, promotion_info_button]
