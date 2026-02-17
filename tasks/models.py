"""
Task Management System - Models
================================
This module defines the data models for the task management application.
"""

from django.db import models
from django.urls import reverse


class Task(models.Model):
    """
    Task Model
    ----------
    Represents a single task/to-do item in the system.
    
    Fields:
        title: The task's title (required, max 200 characters)
        description: Optional detailed description of the task
        is_completed: Boolean flag indicating task completion status
        created_at: Timestamp of task creation (auto-set)
    """
    
    title = models.CharField(
        max_length=200,
        help_text="Enter the task title (max 200 characters)"
    )
    
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional detailed description of the task"
    )
    
    is_completed = models.BooleanField(
        default=False,
        help_text="Mark as True when task is completed"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when task was created"
    )
    
    class Meta:
        """
        Meta options for Task model
        """
        ordering = ['-created_at']  # Most recent tasks first
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    
    def __str__(self):
        """
        String representation of the task
        
        Returns:
            str: The task title
        """
        return self.title
    
    def get_absolute_url(self):
        """
        Returns the URL to access a detail view of the task
        
        Returns:
            str: URL path for task detail view
        """
        return reverse('task-detail', kwargs={'pk': self.pk})
