# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 18:57:46 2016

@author: appertjt
"""

from django.conf.urls import url
from hello_world import views

urlpatterns=[url(r'^$', views.index, name='index'),
             url(r'^about/', views.about, name='about'),
             url(r'^better/$', views.better, name='better'),]
