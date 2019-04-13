#!/usr/bin/python
# encoding:utf-8
from testcase.case_manage import info
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # 下单case
    # suite.addTest(info('shop_card'))
    # 查询订单case
    # suite.addTest(info('select_order'))
    # 查询订单筛选
    # suite.addTest(info('filtrate_order'))
    # 会员中心--搜索会员
    # suite.addTest(info('member_center'))
    # 会员中心--注册会员
    # suite.addTest(info('member_registers'))
    # 调拨入库，高级搜索
    # suite.addTest(info('transfer_search'))
    # 调拨入库，调拨签收
    # suite.addTest(info('transfer_confirm'))
    # 畅销排行
    # suite.addTest(info('bestsell'))
    # 查询报表
    suite.addTest(info('basic_report_act'))
    report_dir = './test_report'
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestReportCN(stream=f, title='测试报告', description='Android ShopForce自动化测试')
        runner.run(suite)
    f.close()
