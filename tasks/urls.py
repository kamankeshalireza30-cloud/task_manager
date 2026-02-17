"""
Task Management System - URL Configuration
==========================================
This module defines all URL patterns for the task management application.
"""

from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleCompleteView
)

urlpatterns = [
    # Task List - Home page
    path('', TaskListView.as_view(), name='task-list'),
    
    # Create new task
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    
    # Update existing task
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-update'),
    
    # Delete task
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    
    # Toggle task completion (AJAX endpoint)
    path('task/<int:pk>/toggle/', TaskToggleCompleteView.as_view(), name='task-toggle'),
]
