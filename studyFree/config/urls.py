"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings  # 新增
from django.conf.urls import url  # 新增
from django.contrib import admin
from django.urls import path, include
from django.views import static  # 新增

import Admin.urls
import Common.urls
import FrontEnd.urls
import Pay.urls
from Common.views import Login, CQ, Download

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign', Login().handler),
    path('cq', CQ().handler),
    path('download', Download().handler),
    path('frontEnd/', include(FrontEnd.urls)),
    path('pay/', include(Pay.urls)),
    path('common/', include(Common.urls)),
    path('my_admin/', include(Admin.urls)),
    # 以下是新增
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),
]
