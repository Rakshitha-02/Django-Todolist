import re
from django.db import models

# Create your models here.
class Todo(models.Model):
    Name = models.CharField(max_length=30)

    Desc= models.CharField(max_length=30)

def __str__(self):
    return self.Name