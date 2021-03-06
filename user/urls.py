from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('get_user_information', views.get_user_information),
    path('change_user_information', views.change_user_information),
    path('upload_avatar', views.upload_avatar),
    path('adduser', views.adduser),
    path('register.html', TemplateView.as_view(template_name = 'register.html')),
    path('login.html', TemplateView.as_view(template_name = 'login.html')),
    path('myprofile.html', TemplateView.as_view(template_name = 'myprofile.html')),
    path('settingpage.html', TemplateView.as_view(template_name = 'settingpage.html')),
    path('upload_avatar.html', TemplateView.as_view(template_name = 'upload_avatar.html')),
    path('set_admin', views.set_admin),
]