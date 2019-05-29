#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from h5_page_location import h5OrderLocation
import time


# ===================>>>>>>>盘点单，调拨单，退货单手工添加商品<<<<<<<<===============================
def add_product(basefunction,product_codes):
    contexts = basefunction.driver.contexts
    basefunction.switch_h5(contexts[1])
    basefunction.click_element(h5OrderLocation.add_handle)
    for code in product_codes:
        contexts = basefunction.driver.contexts
        basefunction.switch_h5(contexts[0])
        time.sleep(7)
        for num in code:
            basefunction.click_acc('%s' % num)
        basefunction.click_acc(h5OrderLocation.search)
        contexts = basefunction.driver.contexts
        basefunction.switch_h5(contexts[1])
        time.sleep(4)
        basefunction.click_element(h5OrderLocation.product_colors)
        basefunction.click_element(h5OrderLocation.product_size)
        basefunction.click_element(h5OrderLocation.add)
    basefunction.click_element(h5OrderLocation.back_btn)
    basefunction.click_element(h5OrderLocation.confirm)
    basefunction.click_element(h5OrderLocation.back_btn)