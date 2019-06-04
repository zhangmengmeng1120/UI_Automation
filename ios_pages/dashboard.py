#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from ios_page_location import basePage
from h5_page_location import dashboardLocation as dbLocation
from h5_pages import dashboard
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')


class Dashboard(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def basic_dashboard_act(self, business, username, password):
        basePage.login(self, business, username, password)
        try:

            self.click_acc(basePage.menu)
            self.click_acc(basePage.dashboard_item_name)
            contexts = self.driver.contexts
            self.switch_h5(contexts[1])
            time.sleep(4)

            # ===================>>>>>>>门店销售<<<<<<<<===============================
            dashboard.shop_sale(self,'ios')
            # ===================>>>>>>>门店指标<<<<<<<<===============================
            dashboard.shop_indicator(self,'ios')
            # ===================>>>>>>>门店周报<<<<<<<<===============================
            dashboard.shop_weekly(self,'ios')
            # ===================>>>>>>>库存分析<<<<<<<<===============================
            dashboard.inventory_indicator(self,'ios')
        except Exception as e:
            print e
            raise Exception('数据罗盘操作出现异常')
    #
    # def shop_sale(self):
    #     self.click_element(dbLocation.shop_sale_button, timeout=4)
    #     # 销售统计
    #     self.click_element(dbLocation.sale_map_datepicker, timeout=1)
    #     self.chose_date('month')
    #
    #     self.driver.execute_script("mobile: swipe", {"direction": "up"})
    #     # basePage.h5_swipe_up(self, 0.5, 0.8, 0.5, 0.5)
    #
    #     # 员工销售统计
    #     self.click_element(dbLocation.employee_sale_datepicker, timeout=1)
    #     self.chose_date('month')
    #
    #     self.driver.execute_script("mobile: swipe", {"direction": "up"})
    #     # basePage.h5_swipe_up(self, 0.5, 0.8, 0.5, 0.5)
    #
    #     # 销售走势
    #     self.click_element(dbLocation.sale_trend_datepicker, timeout=1)
    #     self.chose_date()
    #
    #     # # 时段分析
    #     # self.click_element(dbLocation.peroid_analysis_datepicker, timeout=1)
    #     # self.chose_date()
    #
    # def shop_indicator(self):
    #     self.click_element(dbLocation.shop_indicator_button, timeout=4)
    #     # 门店销售指标
    #     self.click_element(dbLocation.shop_indicator_moredwc_button, timeout=1)
    #     # self.click_element(dbLocation.day_indicator_label, timeout=1)
    #     self.click_element(dbLocation.week_indicator_label, timeout=1)
    #     self.click_element(dbLocation.month_indicator_label, timeout=1)
    #
    #     # basePage.location_click(self, [(0.01, 0.1)], click_time=500)
    #     self.driver.execute_script("mobile: tap", {"element": None,'x':10.0,'y':80.0})
    #
    #     # basePage.h5_swipe_up(self, 0.5, 0.8, 0.5, 0.5)
    #     self.driver.execute_script("mobile: swipe", {"direction": "up"})
    #
    #     # 销售指标K线图
    #     # self.click_element(dbLocation.day_datetap, timeout=1)
    #     self.click_element(dbLocation.week_datetap, timeout=1)
    #     self.click_element(dbLocation.month_datetap, timeout=1)
    #
    #     # basePage.h5_swipe_up(self, 0.5, 0.8, 0.5, 0.1)
    #     self.driver.execute_script("mobile: swipe", {"direction": "up"})
    #
    #     # 店员销售指标
    #     # self.click_element(dbLocation.day_emp_indicator_datetap, timeout=1)
    #     self.click_element(dbLocation.week_emp_indicator_datetap, timeout=1)
    #     self.click_element(dbLocation.month_emp_indicator_datetap, timeout=1)
    #
    # def shop_weekly(self):
    #     self.click_element(dbLocation.shop_weekly_button, timeout=4)
    #
    #     self.click_element(dbLocation.shop_week_datepicker, timeout=1)
    #     self.chose_date('week')
    #
    #     self.click_element(dbLocation.rank_div, timeout=1)
    #     self.click_element(dbLocation.pk_button, timeout=1)
    #
    #     self.driver.execute_script("mobile: swipe", {"direction": "up"})
    #
    #     # basePage.h5_swipe_up(self, 0.5, 0.8, 0.5, 0.4, time_out=1)
    #
    #     self.driver.execute_script("mobile: swipe", {"direction": "up"})
    #
    #     # basePage.h5_swipe_up(self, 0.5, 0.99, 0.5, 0.1, time_out=1)
    #     self.click_element(dbLocation.promotion_product_label, timeout=1)
    #
    # def inventory_indicator(self):
    #     self.click_element(dbLocation.inventory_indicator_button, timeout=4)
    #     self.driver.execute_script("mobile: swipe", {"direction": "up"})
    #     self.driver.execute_script("mobile: swipe", {"direction": "up"})
    #     # basePage.h5_swipe_up(self, 0.5, 0.8, 0.5, 0.2, time_out=3)
    #     # basePage.h5_swipe_up(self, 0.5, 0.8, 0.5, 0.2, time_out=3)
    #
    # def chose_date(self, type='day'):
    #     if type == 'day':
    #         self.click_element(dbLocation.type_day, timeout=1)
    #     elif type == 'week':
    #         self.click_element(dbLocation.type_week, timeout=1)
    #     elif type == 'month':
    #         self.click_element(dbLocation.type_month, timeout=1)
    #     elif type == 'range':
    #         self.click_element(dbLocation.type_range, timeout=1)
    #     self.click_element(dbLocation.first_day, timeout=1)
    #     self.click_element(dbLocation.search_button, timeout=3)
