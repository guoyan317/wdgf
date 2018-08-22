# Created by gy on 2018/8/9.
from __future__ import unicode_literals
from django.conf.urls import url
from portal import views


urlpatterns = [
    # 首页
    url(r'^$', views.gf_index, name='portal_index')
]
