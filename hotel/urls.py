from django.conf.urls import url

from . import views

urlpatterns = [
    # https:127.0.0.1:8000/v1/users
    #获取全部酒店数据
    url(r'^$', views.hotels),
    #获取某用户名下所有酒店数据
    url(r'^/(?P<user_name>[\w]{1,11})$', views.hotels),
    #获取某用户名下单个酒店数据
    url(r'^/(?P<user_name>[\w]{1,11})/(?P<commodityName>[\w]{1,11})$', views.hotels),
    url(r'^/(?P<username>[\w]{1,11})/(?P<commodityName>[\w]{1,11})/avatar$', views.hotel_avatar),

]
