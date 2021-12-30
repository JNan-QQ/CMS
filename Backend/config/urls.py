"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from login.views import FilesUpDown
from userToken.views import user_Token

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # 登录模块
                  path('sign/', include('login.urls')),
                  # 账号管理模块
                  path('account/', include('account.urls')),
                  # 新闻、通知模块
                  path('notice/', include('notice.urls')),
                  # 公共信息
                  path('common/', include('common.urls')),
                  # 文件上传
                  path('files', FilesUpDown().handler),
                  # 网络验证
                  path('Token', user_Token().handler),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
