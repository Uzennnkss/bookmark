"""mysite URL Configuration

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
from django.contrib import admin
# 장고의 내장함수인 url()함수를 가져온다. (아래있는 path들)
from django.urls import path
from bookmark.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',BookmarkLV,name="home"),
    path('detail/<str:id>',BookmarkDV,name="detail"),

]
