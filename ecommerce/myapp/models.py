from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=50)
    description  = models.CharField(max_length=200, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.task_name
    
    
