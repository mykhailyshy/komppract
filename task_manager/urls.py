from django.contrib.auth import views as auth_views
from django.urls import path, include
from tasks.views import register
from django.contrib import admin
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', views.task_list, name='task_list'),
    path('', include('tasks.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', register, name='register'), 
   
]
