from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns += [
    path('api/protected/', views.protected_view, name='protected_view'),
]
urlpatterns += [
    path('api/register/', views. register_user, name='register_user'),
]