from django.contrib import admin
from django.urls import path
from .views import TaskDetailView, TaskAndEventCreateView, TaskUpdateView, EventUpdateView
from . import views
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),
    path('', views.home, name='taskmanager-home'),
    path('about/', views.about, name='taskmanager-about'),
    path('tasks/', views.tasks, name='taskmanager-tasks'),
    path('events/', views.Events, name='taskmanager-events'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('events/<int:pk>', TaskDetailView.as_view(), name='event-detail'),
    path('new/', TaskAndEventCreateView.as_view(), name='new'),
    path('tasks/<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('events/<int:pk>/update', EventUpdateView.as_view(), name='event-update'),
    path('tasks/<int:pk>/delete', views.task_delete, name='task-delete'),
    path('eventss/<int:pk>/delete', views.event_delete, name='event-delete'),
    path('tasks/<int:pk>/complete',
         views.task_mark_as_complete, name='task-completed'),
    path('events/<int:pk>/complete',
         views.event_mark_as_complete, name='event-completed'),
    path('plot/',views.plot,name = 'plot')

]
