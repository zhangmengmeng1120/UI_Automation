#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from page_location import inventoryLocation as inLocation
import basePage
from basePage import login
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Inventory(BaseFunction):
    def __init__(self,driver):
        BaseFunction.__init__(self,driver)

    def inventory_create(self,business,username,password,rack_name):
        '''
        创建盘点单
        :return:
        '''


        login(self, business,username,password)

    def inventory_filtrate(self):
        '''
        根据盘点单状态筛选盘点单
        :return:
        '''






    def inventory_query(self):
        '''
        盘点单高级搜索
        :return:
        '''

