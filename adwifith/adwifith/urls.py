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
from wifi.process import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    # 測試
    path('test', Index.test, name='test'),
    # 流程
    path('index', Index.index, name='index'),
    # path('portal', Portal.portal),
    # path('adv', Adv.adv),
    # path('inurl', Inurl.inurl),
    # path('final', Final.final),
    # 其他
    # path('accsave', Portal.accsave),
    # path('pagecounter', PageCounter.pagecounter),
    # path('agreement', TemplateView.as_view(template_name="agreement.html")),
    # # path('api/', include('backend.urls', namespace='api'))
]
