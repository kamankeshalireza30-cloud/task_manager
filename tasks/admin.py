"""
Task Management System - Admin Configuration
============================================
This module configures the Django admin interface for the Task model.
"""

from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin configuration for Task model
    
    Features:
        - List display with key fields
        - Filtering by completion status and creation date
        - Search functionality
        - Read-only timestamp field
    """
    
    list_display = ('title', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'description')
        }),
        ('Status', {
            'fields': ('is_completed',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
