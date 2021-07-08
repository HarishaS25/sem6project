from django import forms
from .models import TaskAndEvent
from django.contrib.admin.widgets import AdminSplitDateTime


class TaskAndEventCreationForm(forms.ModelForm):
    class meta:
        model = TaskAndEvent
        fields = ['name', 'description', 'due', 'priority', 'name_type']
        date = forms.DateTimeField(widget=AdminSplitDateTime())
