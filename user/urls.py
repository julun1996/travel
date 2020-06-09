from django.conf.urls import url, include
from django.contrib import admin

from user import views

urlpatterns = [
    url(r'^$', views.users),
]
