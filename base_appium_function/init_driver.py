#!/usr/bin/python
# encoding:utf-8
from appium import webdriver
def init_driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '8.1.0',
        'deviceName': '6770047',
        'appPackage': 'com.nexttao.shopforce.test',
        'appActivity': 'com.nexttao.shopforce.fragment.SplashActivity',
        'unicodeKeyboard': 'True',
        'resetKeyboard': 'True'
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver