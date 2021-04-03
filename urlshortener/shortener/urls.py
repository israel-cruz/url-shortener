from django.urls import path

from . import views

urlpatterns = [
    path('', views.shortener, name='shortener'),
    path('<str:pk>', views.go, name='go'),
]