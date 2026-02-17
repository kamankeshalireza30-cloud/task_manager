# tasks/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleCompleteView
)

urlpatterns = [
    # Auth URLs - اضافه کردن صفحات لاگین و رجیستر
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Task URLs
    path('', TaskListView.as_view(), name='task-list'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/toggle/', TaskToggleCompleteView.as_view(), name='task-toggle'),
]