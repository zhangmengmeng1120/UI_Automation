#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from selenium.webdriver.common.by import By
import basePage
import time

class SalePage(BaseFunction):

    def __init__(self,driver):
        BaseFunction.__init__(self,driver)
    # 封装login方法
    def login(self,business,username,password):
        # 输入商户号
        self.input_element(basePage.edit_business,business)
        # 输入用户名
        self.input_element(basePage.edit_username, username)
        # 定位username，防止自动提示导致回删数据
        self.click_element(basePage.edit_username)
        # 输入密码
        self.input_element(basePage.edit_password, password)
        # 点击登录
        self.click_element(basePage.text_login)
        # 验证是否登录成功
        try:
            self.find_element(basePage.shop_title)
            print '登录成功'
        except:
            self.fail('登录失败')


    # 下单操作，购物车页面
    def sale_test(self,business,username,password,product_code,telphone):
        # 商品搜索
        self.keypad_search_btn = (By.ID, 'com.nexttao.shopforce.test:id/keypad_search_btn')
        # 商品尺码
        self.product_sizes = [(By.XPATH,"//android.widget.TextView[contains(@text,'M')]"),(By.XPATH,"//android.widget.TextView[contains(@text,'L')]"),(By.XPATH,"//android.widget.TextView[contains(@text,'XL')]")]
        # 商品颜色
        self.product_colors = [(By.XPATH, "//android.widget.TextView[contains(@text,'黑色')]")]
        # 添加商品
        self.confirm_txt = (By.ID, 'com.nexttao.shopforce.test:id/confirm_txt')
        # 清空购物车
        self.shopcar_clear_btn = (By.ID, 'com.nexttao.shopforce.test:id/shopcar_clear_btn')
        # 确认清空购物车，确认提示信息
        self.text_confirm = (By.ID, 'com.nexttao.shopforce.test:id/text_confirm')
        # 销售员
        self.saleman_text = (By.ID, 'com.nexttao.shopforce.test:id/saleman_text')
        # 第一个销售员的id
        self.tv_sale_name = (By.ID, 'com.nexttao.shopforce.test:id/tv_sale_name')
        # 确认选中的销售员
        self.tv_confirm = (By.ID, 'com.nexttao.shopforce.test:id/tv_confirm')
        # 购物车页面下一步button，去支付button
        self.settle_btn = (By.ID, 'com.nexttao.shopforce.test:id/settle_btn')
        # 用于判断是否进入购物车页面
        self.member_promotion_name = (By.ID, 'com.nexttao.shopforce.test:id/member_promotion_name')
        # 支付方式
        self.pay_cash = (By.XPATH, "//android.widget.TextView[contains(@text,'现金')]")
        # 确认支付
        self.confirm_pay = (By.ID, 'com.nexttao.shopforce.test:id/confirm_pay')
        # 用来判断是否支付完成
        self.img_gou = (By.ID, 'com.nexttao.shopforce.test:id/img_gou')
        # 开始新订单
        self.text_restart = (By.ID, 'com.nexttao.shopforce.test:id/text_restart')

        self.login(business,username,password)
        time.sleep(3)
        # 输入商品编码
        for i in product_code:
            self.driver.press_keycode(basePage.keycode[i])
        self.click_element(self.keypad_search_btn)
        self.click_element(self.product_sizes[0])
        self.click_element(self.product_colors[0])
        self.click_element(self.confirm_txt)
        # 清空购物车
        self.click_element(self.shopcar_clear_btn)
        # 确认清空操作
        self.click_element(self.text_confirm)
        # 商品的颜色和尺码生成唯一的组合
        datagroup = [self.product_colors, self.product_sizes]
        cartesian = basePage.Cartesian(datagroup)
        attrlist = cartesian.assemble()
        for info in attrlist:
            # 输入商品编码
            for i in product_code:
                self.driver.press_keycode(basePage.keycode[i])
            self.click_element(self.keypad_search_btn)
            color_info = info[0]
            size_info = info[1]
            self.click_element(size_info)
            self.click_element(color_info)
            self.click_element(self.confirm_txt)
        # 输入会员手机号码
        for num in telphone:
            self.driver.press_keycode(basePage.keycode[num])
        self.click_element(self.keypad_search_btn)
        # 选择销售员
        self.click_element(self.saleman_text)
        self.click_element(self.tv_sale_name)
        self.click_element(self.tv_confirm)
        # 点击下一步
        self.click_element(self.settle_btn)
        # 确认提示信息
        if self.find_element(self.text_confirm):
            self.click_element(self.text_confirm)
        try:
            # 检查是否进入选择促销的页面
            self.find_element(self.member_promotion_name)
            # 点击去支付
            self.click_element(self.settle_btn)
        except:
            self.fail('上传销售订单出现异常')
        #选择现金支付
        self.click_element(self.pay_cash)
        # 确认支付
        self.click_element(self.confirm_pay)
        try:
            # 检查是否支付成功
            self.find_element(self.img_gou)
            # 开始新订单
            self.click_element(self.text_restart)
            print '支付成功'
        except:
            self.fail('支付出现异常')




