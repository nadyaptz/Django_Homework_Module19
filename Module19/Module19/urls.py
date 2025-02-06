"""
URL configuration for Module19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from task1.views import main_page, anchor, book, info, menu
from task1.views import sign_up_by_html, sign_up_by_django, success_page, news_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', anchor),
    path('lakehouse/', main_page),
    path('lakehouse/book', book),
    path('lakehouse/info', info),
    path('lakehouse/menu', menu),
    path('sign_up_by_html', sign_up_by_html),
    path('sign_up_by_django', sign_up_by_django),
    path('success/', success_page, name='success_page'),
    path('lakehouse/news', news_page),
]
