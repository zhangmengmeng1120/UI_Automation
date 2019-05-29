#!/usr/bin/python
# encoding:utf-8
from ios_page_location.basePage import h5_swipe_up,location_click
from  h5_page_location import dashboardLocation as dbLocation
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



def shop_sale(BaseFunction,device_type):
    BaseFunction.click_element(dbLocation.shop_sale_button, timeout=4)
    # 销售统计
    BaseFunction.click_element(dbLocation.sale_map_datepicker, timeout=1)
    chose_date(BaseFunction,'month')

    if device_type == 'android':
        h5_swipe_up(BaseFunction, 0.5, 0.8, 0.5, 0.5)
    else:
        BaseFunction.driver.execute_script("mobile: swipe", {"direction": "up"})

    # 员工销售统计
    BaseFunction.click_element(dbLocation.employee_sale_datepicker, timeout=1)
    chose_date(BaseFunction,'month')

    if device_type == 'android':
        h5_swipe_up(BaseFunction, 0.5, 0.8, 0.5, 0.5)
    else:
        BaseFunction.driver.execute_script("mobile: swipe", {"direction": "up"})

    # 销售走势
    BaseFunction.click_element(dbLocation.sale_trend_datepicker, timeout=1)
    chose_date(BaseFunction)

    # # 时段分析
    # self.click_element(dbLocation.peroid_analysis_datepicker, timeout=1)
    # self.chose_date()

def shop_indicator(BaseFunction,device_type):
    BaseFunction.click_element(dbLocation.shop_indicator_button, timeout=4)
    # 门店销售指标
    BaseFunction.click_element(dbLocation.shop_indicator_moredwc_button, timeout=1)
    # self.click_element(dbLocation.day_indicator_label, timeout=1)
    BaseFunction.click_element(dbLocation.week_indicator_label, timeout=1)
    BaseFunction.click_element(dbLocation.month_indicator_label, timeout=1)
    if device_type == 'android':
        location_click(BaseFunction, [(0.01, 0.1)], click_time=500)
    else:
        BaseFunction.driver.execute_script("mobile: tap", {"element": None,'x':10.0,'y':80.0})

    if device_type == 'android':
        h5_swipe_up(BaseFunction, 0.5, 0.8, 0.5, 0.5)
    else:
        BaseFunction.driver.execute_script("mobile: swipe", {"direction": "up"})
    # 销售指标K线图
    # self.click_element(dbLocation.day_datetap, timeout=1)
    BaseFunction.click_element(dbLocation.week_datetap, timeout=1)
    BaseFunction.click_element(dbLocation.month_datetap, timeout=1)

    if device_type == 'android':
        h5_swipe_up(BaseFunction, 0.5, 0.8, 0.5, 0.5)
    else:
        BaseFunction.driver.execute_script("mobile: swipe", {"direction": "up"})
    # 店员销售指标
    # self.click_element(dbLocation.day_emp_indicator_datetap, timeout=1)
    BaseFunction.click_element(dbLocation.week_emp_indicator_datetap, timeout=1)
    BaseFunction.click_element(dbLocation.month_emp_indicator_datetap, timeout=1)

def shop_weekly(BaseFunction,device_type):
    BaseFunction.click_element(dbLocation.shop_weekly_button, timeout=4)

    BaseFunction.click_element(dbLocation.shop_week_datepicker, timeout=1)
    chose_date(BaseFunction,'week')

    BaseFunction.click_element(dbLocation.rank_div, timeout=1)
    BaseFunction.click_element(dbLocation.pk_button, timeout=1)

    if device_type == 'android':
        h5_swipe_up(BaseFunction, 0.5, 0.8, 0.5, 0.4)
        h5_swipe_up(BaseFunction, 0.5, 0.99, 0.5, 0.1, time_out=1)

    else:
        BaseFunction.driver.execute_script("mobile: swipe", {"direction": "up"})
    BaseFunction.click_element(dbLocation.promotion_product_label, timeout=1)

def inventory_indicator(BaseFunction,device_type):
    BaseFunction.click_element(dbLocation.inventory_indicator_button, timeout=4)
    if device_type == 'android':
        h5_swipe_up(BaseFunction, 0.5, 0.8, 0.5, 0.2, time_out=3)
        h5_swipe_up(BaseFunction, 0.5, 0.8, 0.5, 0.2, time_out=3)

    else:
        BaseFunction.driver.execute_script("mobile: swipe", {"direction": "up"})

def chose_date(BaseFunction, type='day'):
    if type == 'day':
        BaseFunction.click_element(dbLocation.type_day, timeout=3)
    elif type == 'week':
        BaseFunction.click_element(dbLocation.type_week, timeout=3)
    elif type == 'month':
        BaseFunction.click_element(dbLocation.type_month, timeout=3)
    elif type == 'range':
        BaseFunction.click_element(dbLocation.type_range, timeout=3)
    BaseFunction.click_element(dbLocation.first_day, timeout=1)
    BaseFunction.click_element(dbLocation.search_button, timeout=3)
