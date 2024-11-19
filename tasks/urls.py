from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import custom_logout
from tasks.views import register, home

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('logout/', custom_logout, name='logout'),
    path('home/', home, name='home'),
]
