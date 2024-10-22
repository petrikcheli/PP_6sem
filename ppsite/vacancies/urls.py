from django.urls import path
from . import views
from .views import VacancyCreateView

app_name = 'vacancies'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('search/', views.post_search, name='post_search'),
    path('new/', VacancyCreateView.as_view(), name='vacancy_create'),
]