#!/usr/bin/python
# encoding:utf-8
from h5_page_location import h5OrderLocation
from ios_page_location import basePage
import time


# ===================>>>>>>>盘点单，调拨单，退货单手工添加商品<<<<<<<<===============================
def add_product(basefunction,product_codes,type):
    contexts = basefunction.driver.contexts
    basefunction.switch_h5(contexts[1])
    basefunction.click_element(h5OrderLocation.add_handle[type])
    for code in product_codes:
        contexts = basefunction.driver.contexts
        basefunction.switch_h5(contexts[0])
        time.sleep(7)
        for num in code:
            basefunction.click_acc('%s' % num)
        basefunction.click_acc(basePage.search)
        contexts = basefunction.driver.contexts
        basefunction.switch_h5(contexts[1])
        time.sleep(4)
        basefunction.click_element(h5OrderLocation.product_colors)
        basefunction.click_element(h5OrderLocation.product_size)
        basefunction.click_element(h5OrderLocation.add)
    basefunction.click_element(h5OrderLocation.back_btn)
    basefunction.click_element(h5OrderLocation.confirm)
    basefunction.click_element(h5OrderLocation.back_btn)


def confirm_product(basefunction):
    contexts = basefunction.driver.contexts
    basefunction.switch_h5(contexts[1])
    time.sleep(4)
    basefunction.click_element(h5OrderLocation.icon_edit)
    basefunction.click_element(h5OrderLocation.icon_delete)
    basefunction.click_element(h5OrderLocation.num_key)
    basefunction.click_element(h5OrderLocation.key_confirm)
    basefunction.click_element(h5OrderLocation.btn_save)
    basefunction.click_element(h5OrderLocation.back_btn)
    time.sleep(4)
    contexts = basefunction.driver.contexts
    basefunction.switch_h5(contexts[0])