#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random

# 门店入库button
stock_in = (By.XPATH, "//android.widget.TextView[contains(@text,'门店入库')]")
# 调拨入库button
transfer_in = (By.XPATH, "//android.widget.TextView[contains(@text,'调拨入库')]")
# 确认签收button
take_receive = (By.ID, 'com.nexttao.shopforce.test:id/take_receive')
# 查看详情
details_text = (By.ID, 'com.nexttao.shopforce.test:id/details_text')
# 填写收货数量，这是h5页面

# 调拨单代签收状态
transfer_confirm_state = (By.ID, "com.nexttao.shopforce.test:id/state")
# 调拨单确认签收按钮
transfer_confirm_button = (By.ID, "com.nexttao.shopforce.test:id/take_receive")

# 差异签收弹出框
transfer_diff_wizard = (By.ID, "com.nexttao.shopforce.test:id/multiple_dialog_container")
# 确认签收按钮
text_confirm_button = (By.ID, "com.nexttao.shopforce.test:id/text_confirm")
# 差异收货button
diff_confirm_button = (By.XPATH, "//android.widget.TextView[contains(@text,'差异收货')]")

# 订单状态
state_num = random.randint(1, 4)
order_of_state = (By.XPATH, "//android.widget.TextView[%s]" % state_num)
# 订单状态下拉
title = (By.ID, 'com.nexttao.shopforce.test:id/title')
# 展开订单详情
fold_image = (By.ID, 'com.nexttao.shopforce.test:id/fold_image')

# 高级搜索button
order_search = (By.ID, 'com.nexttao.shopforce.test:id/order_search')
# 查询
search_query = (By.ID, 'com.nexttao.shopforce.test:id/search_query')
# 调拨单号输入框
search_order_no = (By.ID, 'com.nexttao.shopforce.test:id/search_order_no')
# 商品编码输入框
search_order_sku = (By.ID, 'com.nexttao.shopforce.test:id/search_order_sku')
# 发货店仓输入框
search_order_org = (By.ID, 'com.nexttao.shopforce.test:id/search_order_org')
#  调拨类型
type_edit = (By.ID, 'com.nexttao.shopforce.test:id/type_edit')
#  调拨类型option
transfer_options1 = (By.ID, 'com.nexttao.shopforce.test:id/options1')
transfer_options_submit = (By.ID, 'com.nexttao.shopforce.test:id/btnSubmit')

# 日期范围
all_check = (By.ID, 'com.nexttao.shopforce.test:id/all_check')
out_check = (By.ID, 'com.nexttao.shopforce.test:id/out_check')
in_check = (By.ID, 'com.nexttao.shopforce.test:id/in_check')
# 操作人输入框
operate_edit = (By.ID, 'com.nexttao.shopforce.test:id/operate_edit')
# 重置
search_clear = (By.ID, 'com.nexttao.shopforce.test:id/search_clear')
# 取消
search_up_cancel = (By.ID, 'com.nexttao.shopforce.test:id/search_up_cancel')
# 调拨单状态
order_state = (By.XPATH, "//android.widget.TextView[contains(@text,'已完成')]")
# 调拨单号
allocate_name = (By.ID, 'com.nexttao.shopforce.test:id/allocate_name')
# 高级搜索，选择开始日期
start_at = (By.ID, 'com.nexttao.shopforce.test:id/start_at')
# 高级搜索，选择结束日期
end_at = (By.ID, 'com.nexttao.shopforce.test:id/end_at')
# 高级搜索，选择日
day = (By.ID, 'com.nexttao.shopforce.test:id/day')

# H5定位
# 只看差异
btn_view_diff = (By.CLASS_NAME, 'btn-view-diff')
# 搜索button
searchCon = (By.ID, 'searchCon')
# 搜索条件
input_item = (By.CLASS_NAME, 'input-item')
# 清空搜索内容
icon_delete = (By.CLASS_NAME, 'icon-delete')
#

