"""
Task Management System - Views
===============================
This module contains all the view logic using Django's Class-Based Views (CBVs).
"""

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from .models import Task


class TaskListView(ListView):
    """
    Display list of all tasks with statistics
    
    Template: task_list.html
    Context:
        - task_list: QuerySet of all tasks
        - completed_count: Number of completed tasks
        - total_count: Total number of tasks
    """
    
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'task_list'
    
    def get_context_data(self, **kwargs):
        """
        Add additional context data for task statistics
        """
        context = super().get_context_data(**kwargs)
        
        # Calculate task statistics
        all_tasks = Task.objects.all()
        context['total_count'] = all_tasks.count()
        context['completed_count'] = all_tasks.filter(is_completed=True).count()
        context['pending_count'] = all_tasks.filter(is_completed=False).count()
        
        # Calculate completion percentage
        if context['total_count'] > 0:
            context['completion_percentage'] = (
                context['completed_count'] / context['total_count']
            ) * 100
        else:
            context['completion_percentage'] = 0
        
        return context


class TaskCreateView(CreateView):
    """
    Create a new task
    
    Template: task_form.html
    Success URL: Redirects to task list
    """
    
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')
    
    def get_context_data(self, **kwargs):
        """
        Add form title to context
        """
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create New Task'
        context['button_text'] = 'Create Task'
        return context


class TaskUpdateView(UpdateView):
    """
    Update an existing task
    
    Template: task_form.html
    Success URL: Redirects to task list
    """
    
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'is_completed']
    success_url = reverse_lazy('task-list')
    
    def get_context_data(self, **kwargs):
        """
        Add form title to context
        """
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Edit Task'
        context['button_text'] = 'Update Task'
        return context


class TaskDeleteView(DeleteView):
    """
    Delete a task
    
    Template: task_confirm_delete.html
    Success URL: Redirects to task list
    """
    
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')


class TaskToggleCompleteView(View):
    """
    Toggle task completion status without page reload
    
    Accepts: POST request with task ID
    Returns: JSON response with updated status
    """
    
    def post(self, request, pk):
        """
        Handle POST request to toggle task completion
        
        Args:
            request: HTTP request object
            pk: Primary key of the task to toggle
            
        Returns:
            JsonResponse with updated task status
        """
        task = get_object_or_404(Task, pk=pk)
        
        # Toggle the completion status
        task.is_completed = not task.is_completed
        task.save()
        
        # Return JSON response for AJAX requests
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'is_completed': task.is_completed,
                'task_id': task.pk
            })
        
        # Fallback for non-AJAX requests
        return redirect('task-list')
