from django.urls import path
from . import views



app_name = 'tasks'

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/<int:pk>/update/', views.update_task, name='update_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('dashboard/<int:user_id>/', views.dashboard, name='dashboard'),
    path('create-task/', views.create_task, name='create_task'),
    
]

