from typing import ValuesView
from django.urls import path
from . import views
from django.views.static import serve
from django.conf.urls import url

urlpatterns=[
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
]    