from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from task.forms import TaskForm, TagForm
from task.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "task/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.order_by("is_done", "-created_at")

class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task/task_confirm_delete.html"
    success_url = reverse_lazy("task:task-list")


class TagListView(ListView):
    model = Tag
    template_name = "task/tag_list.html"
    context_object_name = "tags"

class TagCreateView(CreateView):
    form_class = TagForm
    template_name = "task/tag_form.html"
    success_url = reverse_lazy("task:tag-list")


class TagUpdateView(UpdateView):
    form_class = TagForm
    template_name = "task/tag_form.html"
    success_url = reverse_lazy("task:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "task/tag_confirm_delete.html"
    success_url = reverse_lazy("task:tag-list")


class TaskStatusView(View):
    def post(self, request, pk) -> HttpResponse:
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect(reverse("task:task-list"))
