from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('about_me/', views.about_me),
    path('', views.landing),
    path('<int:pk>/', views.single_post_page),
    path('',views.index),
    path('', include('single_pages.urls'))
]