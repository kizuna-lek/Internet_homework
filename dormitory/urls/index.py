from django.conf.urls import url
from django.urls import path, include
from dormitory.views.index import index

urlpatterns = [
    path("", index, name="index"),
    path("register", include("dormitory.urls.register.index")),
    path("login", include("dormitory.urls.login.index")),
    path("main", include("dormitory.urls.main.index")),
]
