"""
Task Management System - Models
================================
This module defines the data models for the task management application.
"""

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Task Model
    ----------
    Represents a single task/to-do item in the system.
    
    Fields:
        user: Foreign key to the User model (who owns this task)
        title: The task's title (required, max 200 characters)
        description: Optional detailed description of the task
        completed: Boolean flag indicating task completion status
        created_at: Timestamp of task creation (auto-set)
        updated_at: Timestamp of last update (auto-set)
    """
    
    # ربط تسک به کاربر - این خیلی مهمه!
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # اگه کاربر حذف شد، تسک‌هاش هم حذف بشن
        related_name='tasks',      # دسترسی آسان: user.tasks.all()
        help_text="The user who owns this task"
    )
    
    title = models.CharField(
        max_length=200,
        help_text="Enter the task title (max 200 characters)"
    )
    
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional detailed description of the task"
    )
    
    # تغییر نام از is_completed به completed (ساده‌تر)
    completed = models.BooleanField(
        default=False,
        help_text="Mark as True when task is completed"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when task was created"
    )
    
    # اضافه کردن updated_at (خوبه که داشته باشی)
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when task was last updated"
    )
    
    class Meta:
        """
        Meta options for Task model
        """
        ordering = ['-created_at']  # Most recent tasks first
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        
        # ایندکس برای جستجوی سریع‌تر
        indexes = [
            models.Index(fields=['user', 'completed']),
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        """
        String representation of the task
        
        Returns:
            str: The task title with owner info
        """
        return f"{self.title} - {self.user.username}"
    
    def get_absolute_url(self):
        """
        Returns the URL to access a detail view of the task
        
        Returns:
            str: URL path for task detail view
        """
        return reverse('task-detail', kwargs={'pk': self.pk})
    
    # متدهای کمکی مفید
    def mark_completed(self):
        """Helper method to mark task as completed"""
        self.completed = True
        self.save()
    
    def mark_pending(self):
        """Helper method to mark task as pending"""
        self.completed = False
        self.save()