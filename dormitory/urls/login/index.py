from django.conf.urls import url
from django.urls import path, include
from dormitory.views.login import views

urlpatterns = [
    path("",views.login),
    path("/loginajax/",views.loginajax),
]
