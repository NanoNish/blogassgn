from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('default/', views.index, name='index'),
    path('', include(router.urls)),
    path('login/', views.login, name = 'login'),
]