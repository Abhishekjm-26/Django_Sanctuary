"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,re_path
from hello.views import home, sanctListView
from hello.views import current_datetime, hour_offset, about, contact,add_san,sanctListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('now/',current_datetime),
    re_path(r'^now/(plus|minus)(1)hour/$', hour_offset), 
    re_path(r'^now/(plus|minus)([2-9]|\d\d)hours/$', hour_offset),
    path('about/', about),
    path('contact/', contact),
    path('san/',sanctListView.as_view())
]
urlpatterns += staticfiles_urlpatterns()
