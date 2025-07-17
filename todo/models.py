from django.db import models
import datetime

class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    date = models.DateField(default=datetime.date.today)  # <-- Add default

    def __str__(self):
        return self.title

