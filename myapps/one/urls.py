from django.urls import path

from . import views

urlpatterns = [
    path('template', views.index, name='index'),
]