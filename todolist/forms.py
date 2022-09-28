from django import forms

from todolist.models import ToDoListItem

class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoListItem
        fields = {"title", "description"}
