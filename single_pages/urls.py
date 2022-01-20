from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('about_me/', views.about_me),
    path('',views.landing),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", 
         content_type='text/plain'))
]