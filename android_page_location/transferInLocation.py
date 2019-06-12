#!/usr/bin/python
# encoding:utf-8
from selenium.webdriver.common.by import By
import random
import basePage

# 门店入库button
stock_in = (By.XPATH, "//android.widget.TextView[contains(@text,'门店入库')]")
# 调拨入库button
transfer_in = (By.XPATH, "//android.widget.TextView[contains(@text,'调拨入库')]")
# 确认签收button
take_receive = (By.ID, '%s:id/take_receive'%basePage.package_name)
# 查看详情
details_text = (By.ID, '%s:id/details_text'%basePage.package_name)

# 调拨单代签收状态
transfer_confirm_state = (By.ID, "%s:id/state")

# 差异签收弹出框
transfer_diff_wizard = (By.ID, "%s:id/multiple_dialog_container")
# 确认签收按钮
text_confirm_button = (By.ID, "%s:id/text_confirm")
# 差异收货button
diff_confirm_button = (By.XPATH, "//android.widget.TextView[contains(@text,'差异收货')]")

# 订单状态
state_num = random.randint(1, 4)
order_of_state = (By.XPATH, "//android.widget.TextView[%s]" % state_num)
# 订单状态下拉
title = (By.ID, '%s:id/title'%basePage.package_name)
# 展开订单详情
fold_image = (By.ID, '%s:id/fold_image'%basePage.package_name)

# 高级搜索button
order_search = (By.ID, '%s:id/order_search'%basePage.package_name)
# 查询
search_query = (By.ID, '%s:id/search_query'%basePage.package_name)
# 调拨单号输入框
search_order_no = (By.ID, '%s:id/search_order_no'%basePage.package_name)
# 商品编码输入框
search_order_sku = (By.ID, '%s:id/search_order_sku'%basePage.package_name)
# 发货店仓输入框
search_order_org = (By.ID, '%s:id/search_order_org'%basePage.package_name)
#  调拨类型
type_edit = (By.ID, '%s:id/type_edit'%basePage.package_name)
#  调拨类型option
transfer_options1 = (By.ID, '%s:id/options1'%basePage.package_name)
transfer_options_submit = (By.ID, '%s:id/btnSubmit'%basePage.package_name)

# 日期范围
all_check = (By.ID, '%s:id/all_check'%basePage.package_name)
out_check = (By.ID, '%s:id/out_check'%basePage.package_name)
in_check = (By.ID, '%s:id/in_check'%basePage.package_name)
# 操作人输入框
operate_edit = (By.ID, '%s:id/operate_edit'%basePage.package_name)
# 重置
search_clear = (By.ID, '%s:id/search_clear'%basePage.package_name)
# 取消
search_up_cancel = (By.ID, '%s:id/search_up_cancel'%basePage.package_name)
# 调拨单状态
order_state = (By.XPATH, "//android.widget.TextView[contains(@text,'已完成')]")
# 调拨单号
allocate_name = (By.ID, '%s:id/allocate_name'%basePage.package_name)
# 高级搜索，选择开始日期
start_at = (By.ID, '%s:id/start_at'%basePage.package_name)
# 高级搜索，选择结束日期
end_at = (By.ID, '%s:id/end_at'%basePage.package_name)
# 高级搜索，选择日
day = (By.ID, '%s:id/day'%basePage.package_name)

# H5定位
# 只看差异
btn_view_diff = (By.CLASS_NAME, 'btn-view-diff')
# 搜索button
searchIcon = (By.ID, 'searchIcon')
# 搜索条件
input_item = (By.CLASS_NAME, 'input-item')
# 清空搜索内容
icon_delete = (By.XPATH, "//div[@class='keyboard']/div[1]/img[@class='icon-delete']")
# 返回
back_btn = (By.XPATH, "//div[@class='icon-back']/img[@alt='<']")
# 保存
btn_save = (By.CLASS_NAME, 'btn-save')
# 手工添加
add_handle = (By.XPATH, "//div[@class='before-focus']/div[1]")
# 扫码添加
add_border_node = (By.XPATH, "//div[@class='before-focus']/div[2]")
# 导入采集
loggingimport = (By.XPATH, "//div[@class='before-focus']/div[3]")
# 更多
btn_more = (By.CLASS_NAME, 'btn-more')
# 清空列表
btn_close_native = (By.CLASS_NAME, 'btn-close-native')
# 点击修改收货数量
icon_edit = (By.XPATH, "//table[@class='el-table__body']/tbody[1]/tr[1]/td[3]/div[1]/div[1]/div[2]")
# 填写收货数量
div_num = random.randint(1,9)
num_key = (By.XPATH, "//div[@class='keyboard']/div[2]/div[%s]"%div_num)
num_keys = (By.XPATH, "//div[@class='keyboard']/div[2]")
# 确认修改收货数量
key_confirm = (By.XPATH, "//div[@class='keyboard']/div[2]/div[12]")
# 订单内容
result_item = (By.CLASS_NAME, 'result-item')
