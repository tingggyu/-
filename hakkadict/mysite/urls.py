"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from website.views import *
from django.conf.urls import url
from mysite import settings
from django.views.static import serve



urlpatterns = [
    url(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT},name='static'),
    path('index/', index),
    path('appendix/', appendix),
    path('appendix2/', appendix2),
    path('directions/<str:cat>/<str:sub>/', directions), 
    path('directions/', directions), 
    path('introduction/', introduction),
    path('name_search/', name_search),
    path('news/', news),
    path('news_detail/<int:i_id>/', news_detail),
    path('resource/<str:sub>/', resource),
    path('resource/', resource),
    path('resource_learning/', resource_learning),
    path('resource_download/', resource_download),
    path('search_list/', search_list),
    path('search_notlist/', search_notlist),
    path('search_result/', search_result),
    path('site_search/', site_search),
    path('sitemap/', sitemap),
    path('thesaurus/', thesaurus),
    path('backend_login/', backend_login),
      #for solr
    path('solr_search/', solr_search),
    path('download_resource/', download_resource),
]
