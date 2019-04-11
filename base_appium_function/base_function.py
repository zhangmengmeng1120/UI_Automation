#!/usr/bin/python
# encoding:utf-8
import time
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.switch_to import MobileCommand
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class BaseFunction(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(*loc).is_displayed())
            return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*loc))
        except:
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