"""adwifith URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from wifi.process import Index
from wifi.process import Portal
from wifi.process import Adv
from wifi.process import Inurl
from wifi.process import Final

urlpatterns = [
    path('admin/', admin.site.urls),
    # 測試
    path('test', Index.test, name='test'),
    # 流程
    path('index', Index.index, name='index'),
    path('portal', Portal.portal, name='portal'),
    path('adv', Adv.adv, name='advoutertest'),
    path('inurl', Inurl.inurl, name='inurl'),
    path('final', Final.final, name='final'),
    # 其他
    # path('pagecounter', PageCounter.pagecounter),
    path('agreement', TemplateView.as_view(template_name="agreement.html"), name='agreement'),
    # # path('api/', include('backend.urls', namespace='api'))
]
