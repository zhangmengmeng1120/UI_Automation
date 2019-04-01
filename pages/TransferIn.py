#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from basePage import login
import basePage
import TransferInLoaction as Tlocation
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TransferIn(BaseFunction):
    def __init__(self,driver):
        BaseFunction.__init__(self,driver)

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

    def transfer_confirm(self,business,username,password):
        '''
        签收待签收的单据，高级搜索
        :param business:
        :param username:
        :param password:
        :return:
        '''


    def transfer_filtrate(self):
        return True



    def transfer_query(self,business,username,password,transferin_order):
        '''
        调拨入库单高级搜索,根据调拨单号查询，在待签收状态下搜索已完成的调拨单，通过什么来验证
        :return:
        '''
        # 登录
        login(self, business, username, password)
        time.sleep(5)
        # 点击菜单
        self.click_element(basePage.menu_btn_layout)
        # 向上滑到页面
        self.swipe_up()
        # 点击门店入库
        self.click_element(Tlocation.stock_in)
        # 点击调拨入库
        self.click_element(Tlocation.transfer_in)
        time.sleep(2)
        # 点击高级搜索
        self.click_element(Tlocation.order_search)
        # 输入调拨单号
        self.input_element(Tlocation.search_order_no,transferin_order)
        # 点击查询
        self.click_element(Tlocation.search_query)
        time.sleep(2)
        el = self.find_element(Tlocation.order_state)
        if el:
            if self.find_element(Tlocation.title).text == '待签收' and self.find_element(Tlocation.order_state).text == '已完成' and transferin_order in self.find_element(Tlocation.allocate_name).text:
                print '验证成功'
        else:
            raise Exception('查找元素Tlocation.order_state的结果为%s'%el)






