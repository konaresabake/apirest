from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User , related_name= 'task' , on_delete=models.CASCADE)

    def __init__(self):
        return self.title
        