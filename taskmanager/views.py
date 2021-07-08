from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TaskAndEvent
from django.utils import timezone
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.admin import widgets
from .forms import TaskAndEventCreationForm
from django.contrib import messages
from django import forms


def home(request):
    return render(request, 'taskmanager/home.html')


def about(request):
    return render(request, 'taskmanager/about.html')


@login_required
def tasks(request):
    dues = TaskAndEvent.objects.filter(due__lt=datetime.now(tz=timezone.utc), author=request.user, complete='nc',
                                       name_type=1)
    tasks = TaskAndEvent.objects.filter(due__gt=datetime.now(
        tz=timezone.utc), author=request.user, complete='nc', name_type=1)
    context = {
        'due': dues,
        'tasks': tasks
    }
    return render(request, 'taskmanager/tasks.html', context)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = TaskAndEvent
    form_class = TaskAndEventCreationForm


class TaskAndEventCreateView(LoginRequiredMixin, CreateView):
    model = TaskAndEvent
    fields = ['name', 'description', 'due', 'priority', 'name_type']
    widgets = {
        'due': widgets.AdminSplitDateTime,
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Added successfully')
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskAndEvent
    fields = ['name', 'description', 'due', 'priority', 'name_type']
    widgets = {
        'due': widgets.AdminSplitDateTime,
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Updated successfully')
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskAndEvent
    fields = ['name', 'description', 'due', 'priority', 'name_type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Updated successfully')
        return super().form_valid(form)


@login_required
def Events(request):
    events = TaskAndEvent.objects.filter(author=request.user, complete='nc',
                                         name_type=2)
    context = {
        'events': events
    }
    return render(request, 'taskmanager/events.html', context)


@login_required
def task_delete(request, pk):
    item = TaskAndEvent.objects.filter(id=pk).first()
    item.complete = 'del'
    item.save()
    messages.success(request, 'Task deleted Successfully')
    return redirect('taskmanager-tasks')


@login_required
def event_delete(request, pk):
    item = TaskAndEvent.objects.filter(id=pk).first()
    item.complete = 'del'
    item.save()
    messages.success(request, 'Event deleted Successfully')
    return redirect('taskmanager-events')


@login_required
def task_mark_as_complete(request, pk):
    item = TaskAndEvent.objects.filter(id=pk).first()
    if(item.due > datetime.now(tz=timezone.utc)):
        item.complete = 'ontime'
    else:
        item.complete = 'delayed'
    item.save()
    messages.success(request, 'Task completed')
    return redirect('taskmanager-tasks')


@login_required
def event_mark_as_complete(request, pk):
    item = TaskAndEvent.objects.filter(id=pk).first()
    item.complete = 'ontime'
    item.save()
    messages.success(request, 'Event completed')
    return redirect('taskmanager-events')


@login_required
def plot(request):
    labels = ['deleted', 'completed_on_time', 'delayed', 'not_completed']
    data = []
    deleted = len(TaskAndEvent.objects.filter(
        author=request.user, name_type=1, complete='del'))
    completed = len(TaskAndEvent.objects.filter(
        author=request.user, name_type=1, complete='ontime'))
    delayed = len(TaskAndEvent.objects.filter(
        author=request.user, name_type=1, complete='delayed'))
    not_completed = len(TaskAndEvent.objects.filter(
        author=request.user, name_type=1, complete='nc'))
    data.append(deleted)
    data.append(completed)
    data.append(delayed)
    data.append(not_completed)
    s = sum(data)
    return render(request, 'taskmanager/plot.html', {'labels': labels, 'data': data, 'sum': s})
