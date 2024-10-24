from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', 
        auth_views.LoginView.as_view(template_name='account/registration/login.html'),
        name='login'),
    path('logout/',
        auth_views.LogoutView.as_view(template_name='account/registration/logged_out.html'),
        name='logout'),  
    
    # url-адреса смены пароля
    path('password-change/',
        auth_views.PasswordChangeView.as_view(template_name='account/registration/password_change_form.html'),
        name='password_change'),
    path('password-change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='account/registration/password_change_done.html'),
        name='password_change_done'),

    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
]
