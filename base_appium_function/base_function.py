#!/usr/bin/python
# encoding:utf-8

from selenium.webdriver.support.wait import WebDriverWait

class BaseFunction(object):
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,loc,timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(*loc).is_displayed())
            return WebDriverWait(self.driver,timeout).until(lambda x: x.find_element(*loc))
        except:
            return False

    def click_element(self,loc):
        self.find_element(loc).click()

    def input_element(self,loc,text):
        self.inp = self.find_element(loc)
        self.inp.clear()
        self.inp.send_keys(text)

