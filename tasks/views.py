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
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    """
    Display list of all tasks with statistics
    
    Template: task_list.html
    Context:
        - tasks: QuerySet of all tasks (changed from task_list)
        - completed_tasks: Number of completed tasks (changed from completed_count)
        - total_tasks: Total number of tasks (changed from total_count)
        - pending_tasks: Number of pending tasks (changed from pending_count)
        - completion_percentage: Percentage of completed tasks
    """
    
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'  # Changed to match template
    
    def get_queryset(self):
        """Show only tasks for the current user"""
        return Task.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        """
        Add additional context data for task statistics
        """
        context = super().get_context_data(**kwargs)
        
        # Calculate task statistics for current user only
        user_tasks = self.get_queryset()
        context['total_tasks'] = user_tasks.count()
        context['completed_tasks'] = user_tasks.filter(completed=True).count()  # Changed to completed
        context['pending_tasks'] = user_tasks.filter(completed=False).count()   # Changed to completed
        
        # Calculate completion percentage
        if context['total_tasks'] > 0:
            context['completion_percentage'] = (
                context['completed_tasks'] / context['total_tasks']
            ) * 100
        else:
            context['completion_percentage'] = 0
        
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new task
    
    Template: task_form.html
    Success URL: Redirects to task list
    """
    
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        """Assign the current user to the task"""
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        """
        Add form title to context
        """
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create New Task'
        context['button_text'] = 'Create Task'
        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update an existing task
    
    Template: task_form.html
    Success URL: Redirects to task list
    """
    
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'completed']  # Changed to completed
    success_url = reverse_lazy('task-list')
    
    def get_queryset(self):
        """Ensure users can only update their own tasks"""
        return Task.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        """
        Add form title to context
        """
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Edit Task'
        context['button_text'] = 'Update Task'
        return context


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a task
    
    Template: task_confirm_delete.html
    Success URL: Redirects to task list
    """
    
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
    
    def get_queryset(self):
        """Ensure users can only delete their own tasks"""
        return Task.objects.filter(user=self.request.user)


class TaskToggleCompleteView(LoginRequiredMixin, View):
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
        task = get_object_or_404(Task, pk=pk, user=request.user)  # Add user filter
        
        # Toggle the completion status
        task.completed = not task.completed  # Changed to completed
        task.save()
        
        # Return JSON response for AJAX requests
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'completed': task.completed,  # Changed to completed
                'task_id': task.pk
            })
        
        # Fallback for non-AJAX requests
        return redirect('task-list')