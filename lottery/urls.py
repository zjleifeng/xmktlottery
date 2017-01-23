#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/8 12:35
# @Author  : eric
# @Site    : 
# @File    : urls.py
# @Software: PyCharm


from django.conf.urls import include, url

urlpatterns = [
    url(r'^accounts/login/$', 'lottery.account.login', name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/accounts/login/'}, name="userlogout"),
    url(r'^$', 'lottery.views.index', name='home'),

    url(r'^lot5/$', 'lottery.views.lot5', name='home5'),
    url(r'^update5/$', 'lottery.views.update5', name='update5'),
    url(r'^cho5/$', 'lottery.views.cho5', name='cho5'),

    url(r'^lot4/$', 'lottery.views.lot4', name='home4'),
    url(r'^update4/$', 'lottery.views.update4', name='update4'),
    url(r'^cho4/$', 'lottery.views.cho4', name='cho4'),

    url(r'^lot3/$', 'lottery.views.lot3', name='home3'),
    url(r'^update3/$', 'lottery.views.update3', name='update3'),
    url(r'^cho3/$', 'lottery.views.cho3', name='cho3'),

    url(r'^lot2/$', 'lottery.views.lot2', name='home2'),
    url(r'^update2/$', 'lottery.views.update2', name='update2'),
    url(r'^cho2/$', 'lottery.views.cho2', name='cho2'),

    url(r'^lot1/$', 'lottery.views.lot1', name='home1'),
    url(r'^update1/$', 'lottery.views.update1', name='update1'),
    url(r'^cho1/$', 'lottery.views.cho1', name='cho1'),

    url(r'^lott/$', 'lottery.views.lott', name='homet'),
    url(r'^updatet/$', 'lottery.views.updatet', name='updatet'),
    url(r'^chot/$', 'lottery.views.chot', name='chot'),

    url(r'^lotj1/$', 'lottery.views.lotj1', name='homej1'),
    url(r'^updatej1/$', 'lottery.views.updatej1', name='updatej1'),


    url(r'^lotj2/$', 'lottery.views.lotj2', name='homej2'),
    url(r'^updatej2/$', 'lottery.views.updatej2', name='updatej2'),

    url(r'^result/$', 'lottery.views.result', name='result'),

    url(r'^upname/$','lottery.views.upname',name='upname-view'),
    url(r'^dellottyers/$','lottery.views.dellottyers',name='dellottyers-view'),


    url(r'^initialize/$','lottery.views.initialize',name='initialize'),

]