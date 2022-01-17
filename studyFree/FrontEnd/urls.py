# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2022/1/11 13:08
# @Author    :姜楠
# @Tool      :PyCharm

from django.urls import path
from FrontEnd.views import Article, Note

urlpatterns = [
    path('article', Article().handler),
    path('notebook', Note().handler),
]
