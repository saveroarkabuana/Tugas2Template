from asyncio import Task
from dataclasses import fields
from turtle import title
from django import forms

from todolist.models import ToDoListItem

class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoListItem
        fields = {"title", "description"}
