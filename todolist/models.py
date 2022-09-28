from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class ToDoListItem(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()