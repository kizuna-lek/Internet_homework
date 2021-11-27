from django.conf.urls import url
from django.urls import path, include
from dormitory.views.main import views

urlpatterns = [
    path("",views.hello),
]
