# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2022/1/11 13:08
# @Author    :姜楠
# @Tool      :PyCharm

from django.urls import path

from Admin.views import Account, Orders, Article, NoteBooks, WebConfigs, FileManage

urlpatterns = [
    path('webconfig', WebConfigs().handler),
    path('account', Account().handler),
    path('order', Orders().handler),
    path('article', Article().handler),
    path('notebook', NoteBooks().handler),
    path('files', FileManage().handler),
]
