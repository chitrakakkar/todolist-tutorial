from django.db import models
from django.utils import timezone


#  Table name, has to wrap models.Model to get the functionality of Django.

class todo(models.Model):
    # Task_name will be our task title. Allow only 10 chars.
    # Setting as unique constrain to avoid two tasks with the same name.
    task_name = models.CharField(max_length=100, unique=True)
    task_description = models.TextField(max_length=255)
    date_created = models.DateTimeField()

# Returning the name of the task
    def __unicode__(self):
        return self.task_name

# Telling Django to ordered our tasks by date
    class Meta:
        ordering = ['date_created']
