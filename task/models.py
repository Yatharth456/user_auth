from django.db import models
from django.utils import timezone
from accounts.models import CustomUser 


# Create your models here.
class Task(models.Model):
    PENDING = 0
    DONE = 1
    TODO = 2
    INPROGRESS = 3


    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (DONE, 'Done'),
        (TODO, 'Todo'),
        (INPROGRESS, 'Inprogress'),
    )
    assignee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    reporter = models.ForeignKey(CustomUser, related_name="user", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=512, blank=True)
    comment = models.CharField(max_length=512, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)
    working_hours = models.IntegerField(blank=False, default=2)


class TaskRating(models.Model):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4

    RATE_CHOICES = (
        (ZERO, 'zero'),
        (ONE, 'one'),
        (TWO, 'two'),
        (THREE, 'three'),
        (FOUR, 'four'),

    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=512, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, default=0)



