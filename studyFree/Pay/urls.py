# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2022/1/11 13:08
# @Author    :姜楠
# @Tool      :PyCharm

from django.urls import path

from Pay.ali.aliApi import aliPay
from Pay.views import payConfig, payOrder, payProduct, cdk_view

urlpatterns = [
    path('user', payConfig().handler),
    path('order', payOrder().handler),
    path('product', payProduct().handler),
    path('cdk', cdk_view().handler),
    path('success', aliPay().update_order),
    path('result', aliPay().pay_result),
]
