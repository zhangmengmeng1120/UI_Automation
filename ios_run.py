#!/usr/bin/python
# encoding:utf-8
from testcase.ios_case_manage import info
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()

    # 下单case
    # suite.addTest(info('shop_card'))

    # ===================>>>>>>>查询订单<<<<<<<<===============================
    # 根据小票号查询
    # suite.addTest(info('select_order'))

    # 根据小票号查询
    # suite.addTest(info('select_order_sku'))

    # 订单状态过滤
    # suite.addTest(info('filter_order'))

    # 查询订单筛选
    # suite.addTest(info('filtrate_order'))

    # ===================>>>>>>>会员中心<<<<<<<<===============================
    # 会员中心--搜索会员
    # suite.addTest(info('member_center'))

    # 会员中心--注册会员
    # suite.addTest(info('member_registers'))

    # 数据罗盘
    # suite.addTest(info('basic_dashboard_act'))

    # 畅销排行
    # suite.addTest(info('bestsell'))

    # 查询报表
    # suite.addTest(info('basic_report_act'))

    # ===================>>>>>>>调拨出库<<<<<<<<===============================

    # 调拨入库，高级搜索
    # suite.addTest(info('transfer_search'))
    # 调拨入库，调拨签收
    # suite.addTest(info('transfer_confirm'))

    # ===================>>>>>>>配货收货<<<<<<<<===============================

    # 配货收货单签收
    # suite.addTest(info('delivery_receive'))
    # 配货收货单高级搜索
    # suite.addTest(info('delivery_receive_advanced'))

    # ===================>>>>>>>调拨出库<<<<<<<<===============================

    # 创建调拨出库单
    # suite.addTest(info('transferout_create'))
    # 提交调拨出库单
    # suite.addTest(info('transferout_upload'))
    # 调拨出库单高级搜索
    # suite.addTest(info('transferout_search'))

    # ===================>>>>>>>配货退货<<<<<<<<===============================

    # 配货退货单创建
    # suite.addTest(info('refundCreate'))
    # # 配货退货单出库即发货
    # suite.addTest(info('refundUpload'))
    # 配货退货单高级搜索
    # suite.addTest(info('refund_search'))

    # ===================>>>>>>>云仓订单<<<<<<<<===============================

    # 云仓订单
    # suite.addTest(info('basic_cloud_act'))

    # ===================>>>>>>>补货单<<<<<<<<===============================

    # 补货申请单
    # suite.addTest(info('apply_reload_act'))
    # 补货单审批
    # suite.addTest(info('approve_reload_act'))

    # ===================>>>>>>>损益单<<<<<<<<===============================

    # 库存损益单创建
    # suite.addTest(info('scrapCreate'))
    # 库存损益单提交损益
    suite.addTest(info('scrapUpload'))
    # 库存损益单高级搜索
    # suite.addTest(info('scrap_search'))

    # ===================>>>>>>>盘点<<<<<<<<===============================

    # 创建盘点单
    # suite.addTest(info('inventory_stock_create'))
    # 盘点单高级搜索
    # suite.addTest(info('inventory_stock_query'))
    # 查看盘点明细差异
    # suite.addTest(info('inventory_detail_diff'))

    report_dir = './test_report'
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestReportCN(stream=f, title='测试报告', description='Android ShopForce自动化测试')
        runner.run(suite)
    f.close()
