from django.conf.urls import url

from . import views

urlpatterns = [
    # https:127.0.0.1:8000/v1/users
    url(r'^$', views.tokens),
]
