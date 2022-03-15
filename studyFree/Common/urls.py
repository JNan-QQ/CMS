# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2022/1/11 13:08
# @Author    :姜楠
# @Tool      :PyCharm

from django.urls import path

from Common.views import Others, Accounts, MessageView

urlpatterns = [
    path('other', Others().handler),
    path('account', Accounts().handler),
    path('message', MessageView().handler),
]
