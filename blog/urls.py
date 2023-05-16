from django.urls import path
from . import views

#urls for blog app

#when a path is requested, a view is called to handle the request

#E.g when a user goes to the '' (empty path), the home view is called

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]