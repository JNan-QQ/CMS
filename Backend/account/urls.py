# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2021/11/8 16:23
# @Author    :姜楠
# @Tool      :PyCharm
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Account().handler),
]

if __name__ == "__main__":
    run_code = 0
