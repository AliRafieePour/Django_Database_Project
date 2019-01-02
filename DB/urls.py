# my_project/urls.py
from django.contrib import admin
from django.urls import path, url, include # new
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', auth_views.LoginView.as_view(template_name='registration/login.html')),
]