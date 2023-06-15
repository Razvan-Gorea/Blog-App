"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views # import views from auth app
from django.urls import path, include
from users import views as user_views # import views from users app

#urls for app(s) within this django project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'), # when a user goes to the register path, the register view is called
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), # when a user goes to the login path, the login view is called
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), # when a user goes to the login path, the login view is called
    path('', include('blog.urls')),
]
