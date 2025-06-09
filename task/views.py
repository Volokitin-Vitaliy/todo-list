from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task, Tag
from .forms import TaskForm, TagForm


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task/task_list.html"
    ordering = ['is_done', '-created_at']


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task:task_list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task:task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task/task_confirm_delete.html'
    success_url = reverse_lazy('task:task_list')


class TaskToggleDoneView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect('task:task_list')


class TagListView(ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = 'task/tag_list.html'


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'task/tag_form.html'
    success_url = reverse_lazy('task:tag_list')


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'task/tag_form.html'
    success_url = reverse_lazy('task:tag_list')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'task/tag_confirm_delete.html'
    success_url = reverse_lazy('task:tag_list')

