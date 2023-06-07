from django.db import models
from django.utils import timezone
import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication
class Tag(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name
# Create your models here.
class ToDo(models.Model):
    permission_classes=[IsAuthenticated]
    authentication_classes=[BaseAuthentication]
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    )

    Title=models.CharField(max_length=100,blank=False)
    Description=models.TextField(blank=False)
    Date=models.DateTimeField(auto_now_add=True,blank=False,null=False)
    completed=models.BooleanField(default=False)
    due_date=models.DateField()
    created_on=models.TimeField(auto_now_add=True,null=False,blank=False)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='OPEN')
    tags= models.ManyToManyField(Tag, blank=True)
    def __str__(self) -> str:
        return self.tags