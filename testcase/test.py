#!/usr/bin/python
# encoding:utf-8
import unittest
from appium import webdriver
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import time
from HTMLTestRunner import HTMLTestRunner


class Sale(unittest.TestCase):
    # 脚本初始化，获取操作实例
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.1.1',
            'deviceName': '192.168.56.101:5555',
            'appPackage': 'com.nexttao.shopforce.test',
            'appActivity': 'com.nexttao.shopforce.fragment.SplashActivity',
            'automationName': 'Uiautomator2',
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True',
            'noReset': 'True'
            # 'chromeOptions': {'androidProcess': 'WEBVIEW_com.nexttao.shopforce.test'}
        }
        self.drive = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # desired_caps = {
        #     'platformName': 'Android',
        #     'platformVersion': '4.3',
        #     'deviceName': '192.168.56.101:5555',
        #     'appPackage': 'com.nexttao.shopforce.test',
        #     'appActivity': 'com.nexttao.shopforce.fragment.SplashActivity',
        #     'unicodeKeyboard': 'True',
        #     'resetKeyboard': 'True'
        # }
        # self.drive = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 释放实例，释放资源
    def tearDown(self):
        self.drive.quit()

    def sale_order_create(self):
        # Locate定位一个元素
        # Operate操作一个元素
        time.sleep(10)
        business_info = self.drive.find_element_by_id('edit_business')
        business_mess = business_info.text
        if business_mess:
            business_info.clear()
        business_info.send_keys('crm_test')
        username_info = self.drive.find_element_by_id('edit_username')
        username_mess = username_info.text
        if username_mess:
            username_info.clear()
        username_info.send_keys('pl')
        self.drive.find_element_by_id('edit_username').click()
        self.drive.find_element_by_id('edit_password').send_keys('123')
        time.sleep(2)
        try:
            self.drive.find_element_by_id('text_login').click()
            time.sleep(5)
            self.drive.find_element_by_id('shopcar_title')
            print '登录成功'
        except:
            self.fail(u'登录失败')
        self.drive.press_keycode(8)
        self.drive.press_keycode(15)
        self.drive.press_keycode(9)
        self.drive.press_keycode(8)
        self.drive.press_keycode(7)
        self.drive.press_keycode(8)
        self.drive.press_keycode(9)
        self.drive.find_element_by_id('keypad_search_btn').click()
        time.sleep(2)
        self.drive.find_element_by_xpath(
            "//android.widget.TextView[contains(@text,'M')]").click()
        self.drive.find_element_by_xpath(
            "//android.widget.TextView[contains(@text,'黑色')]").click()
        self.drive.find_element_by_id('confirm_txt').click()
        time.sleep(2)
        self.drive.find_element_by_id('shopcar_clear_btn').click()
        time.sleep(1)
        self.drive.find_element_by_id('text_confirm').click()
        self.assertEqual()
        time.sleep(2)
        self.drive.press_keycode(8)
        self.drive.press_keycode(10)
        self.drive.press_keycode(12)
        self.drive.press_keycode(8)
        self.drive.press_keycode(8)
        self.drive.press_keycode(15)
        self.drive.press_keycode(10)
        self.drive.press_keycode(8)
        self.drive.press_keycode(8)
        self.drive.press_keycode(11)
        self.drive.press_keycode(10)
        self.drive.find_element_by_id('keypad_search_btn').click()
        time.sleep(2)
        self.drive.find_element_by_id('saleman_text').click()
        self.drive.find_element_by_id('tv_sale_name').click()
        self.drive.find_element_by_id('tv_confirm').click()
        time.sleep(2)
        self.drive.press_keycode(8)
        self.drive.press_keycode(15)
        self.drive.press_keycode(9)
        self.drive.press_keycode(8)
        self.drive.press_keycode(7)
        self.drive.press_keycode(8)
        self.drive.press_keycode(9)
        self.drive.find_element_by_id('keypad_search_btn').click()
        time.sleep(2)
        self.drive.find_element_by_xpath(
            "//android.widget.TextView[contains(@text,'L')]").click()
        self.drive.find_element_by_xpath(
            "//android.widget.TextView[contains(@text,'黑色')]").click()
        self.drive.find_element_by_id('confirm_txt').click()
        time.sleep(2)
        self.drive.press_keycode(8)
        self.drive.press_keycode(15)
        self.drive.press_keycode(9)
        self.drive.press_keycode(8)
        self.drive.press_keycode(7)
        self.drive.press_keycode(8)
        self.drive.press_keycode(9)
        self.drive.find_element_by_id('keypad_search_btn').click()
        time.sleep(2)
        self.drive.find_element_by_xpath(
            "//android.widget.TextView[contains(@text,'M')]").click()
        self.drive.find_element_by_xpath(
            "//android.widget.TextView[contains(@text,'黑色')]").click()
        self.drive.find_element_by_id('confirm_txt').click()
        time.sleep(2)
        self.drive.press_keycode(8)
        self.drive.press_keycode(15)
        self.drive.press_keycode(9)
        self.drive.press_keycode(8)
        self.drive.press_keycode(7)
        self.drive.press_keycode(8)
        self.drive.press_keycode(9)
        self.drive.find_element_by_id('keypad_search_btn').click()
        time.sleep(2)
        self.drive.find_element_by_xpath(
            "//android.widget.TextView[contains(@text,'XL')]").click()
        self.drive.find_element_by_xpath(
            "//android.widget.TextView[contains(@text,'黑色')]").click()
        self.drive.find_element_by_id('confirm_txt').click()
        time.sleep(2)
        self.drive.find_element_by_id('settle_btn').click()
        time.sleep(2)
        if self.drive.find_element_by_id('text_title'):
            self.drive.find_element_by_id('text_confirm').click()
        time.sleep(4)
        self.drive.find_element_by_id('settle_btn').click()
        time.sleep(2)
        self.drive.find_element_by_xpath(
            "//android.widget.TextView[contains(@text,'现金')]").click()
        time.sleep(2)
        self.drive.find_element_by_id('confirm_pay').click()
        time.sleep(5)
        try:
            self.drive.find_element_by_id('img_gou')
            print '订单支付完成'
            self.drive.find_element_by_id('text_restart').click()
        except:
            self.fail('支付失败')
        time.sleep(5)

    # 登录--密码错误
    def login_password_error(self):
        self.assertTrue()
        time.sleep(10)
        business_info = self.drive.find_element_by_id('edit_business')
        business_mess = business_info.text
        if business_mess:
            business_info.clear()
        business_info.send_keys('crm_test')
        username_info = self.drive.find_element_by_id('edit_username')
        username_mess = username_info.text
        if username_mess:
            username_info.clear()
        username_info.send_keys('pl')
        self.drive.find_element_by_id('edit_username').click()
        self.drive.find_element_by_id('edit_password').send_keys('111')
        self.drive.find_element_by_css_selector()
        self.drive.scroll()
        self.drive.swipe()
        time.sleep(2)

        try:
            self.drive.find_element_by_id('text_login').click()
            time.sleep(10)
            point_info = self.drive.find_element_by_id('hint_text').text
            print '!!!!!!!!!!!!%s' % point_info
            self.assertEquals('登录失败,用户名/密码错误', point_info)
            tamp = int(time.time())
            filename = '../screenshot/%s%s.png' % ('screenshot', tamp)
            print '截图路径%s' % filename
            self.drive.get_screenshot_as_file(filename)

        except:
            self.fail(u'程序运行异常')

    def h5_test(self):
        time.sleep(10)
        username_info = self.drive.find_element_by_id('edit_username')
        print username_info
        username_info.clear()
        username_info.send_keys('pl')
        username_info.click()
        self.drive.find_element_by_id('edit_password').send_keys('123')
        self.drive.find_element_by_id('text_login').click()
        # time.sleep(2)
        # try:
        #     self.drive.find_element_by_id('text_login').click()
        #     time.sleep(5)
        #     self.drive.find_element_by_id('shopcar_title')
        #     print '登录成功'
        # except:
        #     self.fail(u'登录失败')
        time.sleep(20)
        self.drive.find_element_by_id('menu_btn_layout').click()
        self.drive.find_element_by_xpath("//android.widget.TextView[contains(@text,'畅销排行')]").click()
        time.sleep(5)
        contexts = self.drive.contexts
        print contexts
        self.drive.switch_to.context(contexts[1])
        time.sleep(4)
        now = self.drive.current_context
        print now




if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite.addTest(Sale("sale_order_create"))
    # suite.addTest(Login("login_password_error"))
    suite.addTest(Sale("h5_test"))
    report_dir = '../test_report'
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestReportCN(stream=f, title='测试报告', description='Android ShopForce自动化测试')
        runner.run(suite)
    f.close()
