from django.contrib import admin
from django.urls import path

from cine import views
from cine import views


app_name="cine"
urlpatterns = [
    path('',views.home,name="home"),

    path('add', views.addfilms, name="add"),
    path('filmdetail/<int:p>' ,views.filmdetail,name="filmdetail"),

    path('filmedit/<int:p>', views.filmedit, name="filmedit"),

    path('filmdelete/<int:p>', views.filmdelete, name="filmdelete"),




    ]