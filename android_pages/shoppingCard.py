#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from android_page_location import shoppingCardLocation as scLocation
import basePage
from basePage import login,swipe_up,GetPageSize
import time


class SalePage(BaseFunction):

    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    # 下单操作，购物车页面
    def sale_test(self, business, username, password, product_code, telphone):

        login(self, business, username, password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            print update_info
            time.sleep(2)
            if update_info == False: break
        try:
            # 输入商品编码
            for i in product_code:
                self.driver.press_keycode(basePage.keycode[i])
            self.click_element(basePage.keypad_search_btn)
            self.click_element(scLocation.product_sizes[0])
            self.click_element(scLocation.product_colors[0])
            self.click_element(scLocation.confirm_txt)
            # 清空购物车
            self.click_element(scLocation.shopcar_clear_btn)
            # 确认清空操作
            self.click_element(scLocation.text_confirm)
            # 商品的颜色和尺码生成唯一的组合
            datagroup = [scLocation.product_colors, scLocation.product_sizes]
            cartesian = basePage.Cartesian(datagroup)
            attrlist = cartesian.assemble()
            for info in attrlist:
                # 输入商品编码
                for i in product_code:
                    self.driver.press_keycode(basePage.keycode[i])
                self.click_element(basePage.keypad_search_btn)
                color_info = info[0]
                size_info = info[1]
                self.click_element(size_info)
                self.click_element(color_info)
                self.click_element(scLocation.confirm_txt)
            # 输入会员手机号码
            for num in telphone:
                self.driver.press_keycode(basePage.keycode[num])
            self.click_element(basePage.keypad_search_btn)
            # 选择销售员
            self.click_element(scLocation.saleman_text)
            self.click_element(scLocation.tv_sale_name)
            self.click_element(scLocation.tv_confirm)
            # 点击下一步
            self.click_element(scLocation.settle_btn)
            # 确认提示信息
            if self.find_element(scLocation.text_confirm):
                self.click_element(scLocation.text_confirm)
            try:
                # 检查是否进入选择促销的页面
                self.find_element(scLocation.member_promotion_name)
                # 点击去支付
                self.click_element(scLocation.settle_btn)
            except:
                raise Exception('上传销售订单出现异常')
            # 选择现金支付
            self.click_element(scLocation.pay_cash)
            # 确认支付
            self.click_element(scLocation.confirm_pay)
            try:
                # 检查是否支付成功
                self.find_element(scLocation.img_gou)
                # 开始新订单
                self.click_element(scLocation.text_restart)
                print '支付成功'
            except:
                raise Exception('支付出现异常')
            self.click_element(basePage.menu_btn_layout)
            page_size = GetPageSize(self)
            swipe_up(self, page_size, 0.1, 0.80, 0.1, 0.10)
            self.click_element(basePage.logout)
            self.click_element(basePage.text_confirm)
        except Exception as e:
            raise Exception('创建销售订单出现异常:%s'%e)
