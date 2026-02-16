"""
Task Management System - App Configuration
==========================================
Django app configuration for the tasks application.
"""

from django.apps import AppConfig


class TasksConfig(AppConfig):
    """
    Configuration class for the Tasks application
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
    verbose_name = 'Task Management'
