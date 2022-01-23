# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2022/1/11 13:08
# @Author    :姜楠
# @Tool      :PyCharm

from django.urls import path

from Pay.views import payConfig, payOrder

urlpatterns = [
    path('user', payConfig().handler),
    path('order', payOrder().handler),
]
