#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from selenium.webdriver.common.by import By
import basePage
import time
import random

class QuerySaleOrder(BaseFunction):
    def __init__(self,driver):
        BaseFunction.__init__(self,driver)

    def login(self,business,username,password):
        # 输入商户号
        self.input_element(basePage.edit_business,business)
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

    # 获取屏幕尺寸
    def GetPageSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 上拉加载更多
    def swipe_up(self):
        s = self.GetPageSize()
        sx = s[0] * 0.1
        sy = s[1] * 0.75
        ex = s[0] * 0.1
        ey = s[1] * 0.25
        self.driver.swipe(sx, sy, ex, ey, '500')
    # 下拉刷新
    def swipe_down(self):
        s = self.GetPageSize()
        sx = s[0] * 0.1
        sy = s[1] * 0.2
        ex = s[0] * 0.1
        ey = s[1] * 0.62
        self.driver.swipe(sx, sy, ex, ey, '500')


    def search_order_info(self,business,username,password,order_no):
        '''
        下拉刷新，上拉加载，根据订单号模糊搜索订单
        :param business: 商户号
        :param username: 用户名
        :param password: 密码
        :param order_no: 订单号，用于高级搜索
        :return:
        '''
        # 查询订单button
        self.module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'查询订单')]")
        # 扫描订单编号
        self.scan_layout = (By.ID, 'com.nexttao.shopforce.test:id/scan_layout')
        # 定位第一个销售订单的位置
        self.order_list_item_layout = (By.ID, 'com.nexttao.shopforce.test:id/order_list_item_layout')
        # 高级搜索页面
        self.order_search = (By.ID, 'com.nexttao.shopforce.test:id/order_search')
        # 小票输入框
        self.search_order_no = (By.ID, 'com.nexttao.shopforce.test:id/search_order_no')
        # 搜索button
        self.search_query = (By.ID, 'com.nexttao.shopforce.test:id/search_query')
        # 重置button
        self.search_clear = (By.ID, 'com.nexttao.shopforce.test:id/search_clear')
        # 展开订单信息
        self.fold_image = (By.ID, 'com.nexttao.shopforce.test:id/fold_image')

        # 登录
        self.login(business,username,password)
        time.sleep(3)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
        # 点击查询订单
        self.click_element(self.module_item_name)
        try:
            self.find_element(self.scan_layout)
        except:
            self.fail('进入查询订单页面出现异常')
        time.sleep(10)
        # 展开订单信息
        self.click_element(self.fold_image)
        # 下拉刷新
        self.swipe_down()
        time.sleep(10)
        for i in range(3):
            # 上拉加载
            self.swipe_up()
            time.sleep(3)
        # 点击高级搜索
        self.click_element(self.order_search)
        # 输入搜索内容，小票号
        self.input_element(self.search_order_no,order_no)
        # 清空搜索内容
        self.click_element(self.search_clear)
        if self.find_element(self.search_order_no).text=='请输入销售订单号':
            print '内容清空完成'
        # 输入搜索内容，小票号
        self.input_element(self.search_order_no, order_no)
        # 点击搜索
        self.click_element(self.search_query)
        time.sleep(3)
        # 退出搜索
        self.swipe_down()

    def filtrate_order(self,business,username,password):
        '''
        根据订单状态筛选订单
        '''
        # 查询订单button
        self.module_item_name = (By.XPATH, "//android.widget.TextView[contains(@text,'查询订单')]")
        # 扫描订单编号
        self.scan_layout = (By.ID, 'com.nexttao.shopforce.test:id/scan_layout')
        # 点击全部订单
        self.query_order_title = (By.ID, 'com.nexttao.shopforce.test:id/query_order_title')
        # 订单状态
        state_num = random.randint(1,4)
        self.order_of_state = (By.XPATH, "//android.widget.TextView[%s]"%state_num)
        # 退货订单状态的上一级id
        num = random.randint(1,10)
        self.refund_order = (By.XPATH, "//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[%s]/android.widget.LinearLayout[1]/android.widget.TextView[2]"%num)
        self.exchange_order = (By.XPATH, "//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[%s]/android.widget.LinearLayout[1]/android.widget.TextView[2]"%num)


        # 登录
        self.login(business, username, password)
        time.sleep(3)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
        # 点击查询订单
        self.click_element(self.module_item_name)
        try:
            self.find_element(self.scan_layout)
        except:
            print '进入查询订单页面出现异常'
        time.sleep(5)
        # 点击全部订单
        self.click_element(self.query_order_title)
        # 随机选择全部订单、普通订单、退货订单、换货订单
        self.click_element(self.order_of_state)
        if self.find_element(self.query_order_title).text=='退货订单':
            if self.find_element(self.refund_order).text =='退':
                print '订单筛选正常'
            else:
                print '订单筛选异常'
        elif self.find_element(self.query_order_title).text=='换货订单':
            if self.find_element(self.exchange_order).text == '换':
                print '订单筛选正常'
            else:
                print '订单筛选异常'
        time.sleep(5)






