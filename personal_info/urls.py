
from django.urls import path
from django.conf.urls import include, url, handler404, handler500
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pi/', views.pi, name='pi'),
    url(r'^dashboard/$', views.dashboard, name='dashboard')
  
]