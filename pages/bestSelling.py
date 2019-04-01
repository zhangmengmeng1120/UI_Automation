#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from selenium.webdriver.common.by import By
import basePage
import time
import random
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class BestSelling(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def login(self, business, username, password):
        # 输入商户号
        self.input_element(basePage.edit_business, business)
        # 输入用户名
        self.input_element(basePage.edit_username, username)
        # 定位username，防止自动提示导致回删数据
        self.click_element(basePage.edit_username)
        # 输入密码
        self.input_element(basePage.edit_password, password)
        # 点击登录
        self.click_element(basePage.text_login)
        # 验证是否登录成功
        try:
            self.find_element(basePage.shop_title)
            print '登录成功'
        except:
            self.fail('登录失败')

    def best_info(self):
        # 畅销排行button
        self.module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'畅销排行')]")
        # 搜索button
        self.search_product_btn = (By.ID, 'com.nexttao.shopforce.test:id/search_product_btn')
