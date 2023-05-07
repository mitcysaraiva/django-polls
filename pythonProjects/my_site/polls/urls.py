from django.urls import path 
from . import views 
#nao sei se isso é aqui
from django.contrib import admin 
from django.urls import include, path

urlpatterns = [
    path("", views.index, name= "index"),
    #nem isso
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls)
]