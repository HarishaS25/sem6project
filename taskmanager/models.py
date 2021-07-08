from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse


class TaskAndEvent(models.Model):
    PRIORITIES = ((10, 'high'), (5, 'low'))
    TYPE = ((1, 'Task'), (2, 'Event'))
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    due = models.DateTimeField(
        auto_now_add=False, auto_now=False, default=datetime.now())
    complete = models.CharField(default='nc', max_length=10)
    priority = models.IntegerField(choices=PRIORITIES, default=5)
    name_type = models.IntegerField(choices=TYPE, default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('taskmanager-tasks')
