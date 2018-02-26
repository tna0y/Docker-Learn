from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(User, editable=False, on_delete=None)
    completed = models.BooleanField()
    #id = models.AutoField(primary_key=True)
