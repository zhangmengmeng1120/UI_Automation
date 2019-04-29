#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random
from pages import basePage

# 云仓订单
module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'云仓订单')]")

# ===================>>>>>>>我的云单<<<<<<<<===============================
my_cloud_order_item = (By.XPATH, "//android.widget.TextView[contains(@text,'我的云单')]")

order_state_title = (By.ID, "com.nexttao.shopforce.test:id/cloud_title")

distributed_order_state = (By.XPATH, "//android.widget.TextView[contains(@text,'待分配')]")
ready_order_state = (By.XPATH, "//android.widget.TextView[contains(@text,'待发货')]")
transfered_order_state = (By.XPATH, "//android.widget.TextView[contains(@text,'已发货')]")
canceled_order_state = (By.XPATH, "//android.widget.TextView[contains(@text,'已取消')]")



# ===================>>>>>>>我要发货<<<<<<<<===============================

my_cloud_transfer_item = (By.XPATH, "//android.widget.TextView[contains(@text,'我要发货')]")
