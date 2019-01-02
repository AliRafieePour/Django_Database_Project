"""DB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# my_project/urls.py






from django.contrib import admin
from django.urls import path, include # new
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from main.views import students, admins, majors, dorms, rooms, dept, insert_students, success, insert_admins, insert_dorms, insert_rooms, insert_majors
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view, name='logout'),
#    path('hhh/', LoginView.as_view(template_name='registration/login.html')),
    path('accounts/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('students/', students, name='students'),
    path('admins/', admins, name='admins'),
    path('majors/', majors, name='majors'),
    path('dormitories/', dorms, name='dormitories'),
    path('rooms/', rooms, name='rooms'),
    path('departments/', dept, name='departments'),
    path('insertstudents/', insert_students,  name='insertstudents'),
    path('insertstudents/success/', success),
    path('insertadmins/', insert_admins, name='insertadmins'),
    path('insertadmins/success/', success),
    path('insertdorms/', insert_dorms, name='insertdorms'),
    path('insertdorms/success/', success),
    path('insertrooms/', insert_rooms, name='insertrooms'),
    path('insertrooms/success/', success),
    path('insertmajors/', insert_majors, name='insertmajors'),
    path('insertmajors/success/', success),
    path('updateadmin/', views.addadmin, name='updateadmin'),
    path('updatestudent/', views.updatestudent, name='updatestudent'),
    path('updateroom/', views.updateroom, name='updateroom'),
]