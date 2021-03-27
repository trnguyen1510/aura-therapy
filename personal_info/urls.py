from django.urls import path
from django.conf.urls import include, url, handler404, handler500
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('pi/', views.pi, name='pi'),
    path('therapist/', views.pi, name='therapist')
    ]