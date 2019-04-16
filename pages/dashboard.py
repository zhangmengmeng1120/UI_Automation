#!/usr/bin/python
# encoding:utf-8
from base_appium_function.base_function import BaseFunction
from basePage import login, swipe_up, GetPageSize, h5_swipe_up, location_click
from page_location import dashboardLocation as dbLocation
import basePage
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')


class Dashboard(BaseFunction):
    def __init__(self, driver):
        BaseFunction.__init__(self, driver)

    def basic_dashboard_act(self, business, username, password):
        login(self, business, username, password)
        self.driver.wait_activity(".bash.ui.MainActivity", 10)
        while True:
            update_info = self.find_element(basePage.update_text_info)
            time.sleep(2)
            if not update_info: break
        try:

            self.click_element(basePage.menu_btn_layout)
            self.click_element(dbLocation.module_item_name, timeout=4)
            contexts = self.driver.contexts
            self.driver.switch_to.context(contexts[1])
            time.sleep(4)

            # ===================>>>>>>>门店销售<<<<<<<<===============================
            self.shop_sale()
            # ===================>>>>>>>门店指标<<<<<<<<===============================
            self.shop_indicator()
            # ===================>>>>>>>门店周报<<<<<<<<===============================
            self.shop_weekly()
            # ===================>>>>>>>库存分析<<<<<<<<===============================
            self.inventory_indicator()
        except Exception as e:
            print e
            raise Exception('报表查询操作出现异常')

    def shop_sale(self):
        self.click_element(dbLocation.shop_sale_button, timeout=4)
        # 销售统计
        self.click_element(dbLocation.sale_map_datepicker, timeout=1)
        self.chose_date('month')

        h5_swipe_up(self, 0.5, 0.8, 0.5, 0.5)

        # 员工销售统计
        self.click_element(dbLocation.employee_sale_datepicker, timeout=1)
        self.chose_date('month')

        h5_swipe_up(self, 0.5, 0.8, 0.5, 0.5)

        # 销售走势
        self.click_element(dbLocation.sale_trend_datepicker, timeout=1)
        self.chose_date()

        # # 时段分析
        # self.click_element(dbLocation.peroid_analysis_datepicker, timeout=1)
        # self.chose_date()

    def shop_indicator(self):
        self.click_element(dbLocation.shop_indicator_button, timeout=4)
        # 门店销售指标
        self.click_element(dbLocation.shop_indicator_moredwc_button, timeout=1)
        # self.click_element(dbLocation.day_indicator_label, timeout=1)
        self.click_element(dbLocation.week_indicator_label, timeout=1)
        self.click_element(dbLocation.month_indicator_label, timeout=1)

        location_click(self, [(0.01, 0.1)], click_time=500)

        h5_swipe_up(self, 0.5, 0.8, 0.5, 0.5)
        # 销售指标K线图
        # self.click_element(dbLocation.day_datetap, timeout=1)
        self.click_element(dbLocation.week_datetap, timeout=1)
        self.click_element(dbLocation.month_datetap, timeout=1)

        h5_swipe_up(self, 0.5, 0.8, 0.5, 0.1)
        # 店员销售指标
        # self.click_element(dbLocation.day_emp_indicator_datetap, timeout=1)
        self.click_element(dbLocation.week_emp_indicator_datetap, timeout=1)
        self.click_element(dbLocation.month_emp_indicator_datetap, timeout=1)

    def shop_weekly(self):
        self.click_element(dbLocation.shop_weekly_button, timeout=4)

        self.click_element(dbLocation.shop_week_datepicker, timeout=1)
        self.chose_date('week')

        self.click_element(dbLocation.rank_div, timeout=1)
        self.click_element(dbLocation.pk_button, timeout=1)

        h5_swipe_up(self, 0.5, 0.8, 0.5, 0.4, time_out=1)

        h5_swipe_up(self, 0.5, 0.99, 0.5, 0.1, time_out=1)
        self.click_element(dbLocation.promotion_product_label, timeout=1)

    def inventory_indicator(self):
        self.click_element(dbLocation.inventory_indicator_button, timeout=4)
        h5_swipe_up(self, 0.5, 0.8, 0.5, 0.2, time_out=3)
        h5_swipe_up(self, 0.5, 0.8, 0.5, 0.2, time_out=3)

    def chose_date(self, type='day'):
        if type == 'day':
            self.click_element(dbLocation.type_day, timeout=1)
        elif type == 'week':
            self.click_element(dbLocation.type_week, timeout=1)
        elif type == 'month':
            self.click_element(dbLocation.type_month, timeout=1)
        elif type == 'range':
            self.click_element(dbLocation.type_range, timeout=1)
        self.click_element(dbLocation.first_day, timeout=1)
        self.click_element(dbLocation.search_button, timeout=3)
