from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=1000, null=True, blank=True)
    task_desc = models.TextField(null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)