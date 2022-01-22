from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('about_me/', views.about_me),
    path('',views.landing),
    path('robots.txt/', views.robots),
]