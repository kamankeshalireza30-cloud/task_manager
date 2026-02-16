from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = self.get_queryset()
        total_tasks = tasks.count()
        completed_tasks = tasks.filter(completed=True).count()
        
        context['total_tasks'] = total_tasks
        context['completed_tasks'] = completed_tasks
        context['pending_tasks'] = total_tasks - completed_tasks
        context['completion_percentage'] = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        return context

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

def toggle_complete(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        task.save()
        return JsonResponse({
            'completed': task.completed,
            'success': True
        })
    return JsonResponse({'error': 'Method not allowed'}, status=405)