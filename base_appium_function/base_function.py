#!/usr/bin/python
# encoding:utf-8
import time
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.switch_to import MobileCommand
from appium.webdriver.common.mobileby import MobileBy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class BaseFunction(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(*loc).is_displayed())
            return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*loc))
            # WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc))
            # return self.driver.find_element(*loc)
        except:
            return False

    def find_elements(self, loc):
        '''封装一组元素定位方法'''
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except Exception as e:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))
            return False

    def click_element(self, loc, timeout=1):
        self.find_element(loc).click()
        time.sleep(timeout)

    def input_element(self, loc, text):
        self.inp = self.find_element(loc)
        self.inp.clear()
        self.inp.send_keys(text)

    # Native APP 与H5的切换
    def switch_h5(self, context_name):
        """
        Sets the context for the current session.

        :Args:
         - context_name: The name of the context to switch to.

        :Usage:
            driver.switch_to.context('WEBVIEW_1')
        """
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {'name': context_name})


    def find_element_by_accessibility_id(self, accessibility_id):
        """Finds an element by accessibility id.

        :Args:
         - accessibility_id - a string corresponding to a recursive element search using the
         Id/Name that the native Accessibility options utilize

        :Usage:
            driver.find_element_by_accessibility_id()
        """
        return self.driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value=accessibility_id)

    def click_acc(self,accessibility_id):
        self.find_element_by_accessibility_id(accessibility_id).click()
        time.sleep(1)

    def input_by_acc(self,accessibility_id,text):
        self.inp = self.find_element_by_accessibility_id(accessibility_id)
        self.inp.clear()
        self.inp.send_keys(text)