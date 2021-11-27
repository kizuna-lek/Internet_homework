from django.conf.urls import url
from django.urls import path, include
from dormitory.views.register import views

urlpatterns = [
    path("",views.register),
    path("/registerajax/",views.registerajax),
]
