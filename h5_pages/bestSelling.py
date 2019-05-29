#!/usr/bin/python
# encoding:utf-8
from h5_page_location import bestSellingLocation as bsLocation
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')



def best_info(BaseFunction,product_code):
    contexts = BaseFunction.driver.contexts
    BaseFunction.switch_h5(contexts[1])
    BaseFunction.click_element(bsLocation.search_product_btn)
    BaseFunction.input_element(bsLocation.input_product,product_code)
    BaseFunction.click_element(bsLocation.search)
    time.sleep(2)
    BaseFunction.click_element(bsLocation.clear)
    BaseFunction.click_element(bsLocation.cancel)
    el = BaseFunction.find_element(bsLocation.favourite_product)
    if el:
        BaseFunction.click_element(bsLocation.favourite_product)
        time.sleep(5)
        BaseFunction.click_element(bsLocation.inventory)
        time.sleep(2)
        BaseFunction.click_element(bsLocation.back_btn)
    contexts = BaseFunction.driver.contexts
    BaseFunction.switch_h5(contexts[0])
    time.sleep(5)




