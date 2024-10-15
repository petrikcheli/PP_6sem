from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', 
        auth_views.LoginView.as_view(template_name='account/registration/login.html'),
        name='login'),
    path('logout/',
        auth_views.LogoutView.as_view(template_name='account/registration/logged_out.html'),
        name='logout'),  
    
    path('', views.dashboard, name='dashboard'),
]