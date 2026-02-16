"""
URL configuration for task_manager project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # مسیر اصلی به اپ tasks
]