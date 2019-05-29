#!/usr/bin/python
# encoding:utf-8
from appium import webdriver
def init_driver():
    desired_caps = {
        "bundleId": "com.nexttao.shopforcetest",
        "platformName": "iOS",
        "automationName": "XCUITest",
        "platformVersion": "12.2",
        "deviceName": "iPad mini 2",
        "noReset": True,
        "udid": "0ad4f1206d89a16b6666540333e6f3779582c20d",
        "showXcodeLog":True
        # "startIWDP":True,
        # "newCommandTimeout":360,
        # "wdaLaunchTimeout":240000,
        # "wdaConnectionTimeout":240000
        }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver