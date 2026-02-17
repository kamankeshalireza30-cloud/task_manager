# tasks/admin.py
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin configuration for Task model
    """
    list_display = ['title', 'user', 'completed', 'created_at']
    list_filter = ['completed', 'created_at', 'user']
    search_fields = ['title', 'description', 'user__username']
    list_editable = ['completed']
    list_per_page = 20
    
    fieldsets = (
        ('Task Information', {
            'fields': ('user', 'title', 'description')
        }),
        ('Status', {
            'fields': ('completed',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']