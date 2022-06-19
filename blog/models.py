from collections import UserList
from time import timezone
from turtle import title
from typing import Text
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Post(models.Model):
    Title:models.CharField(max_length=200)
    Text:models.TimeField()
    Author=models.ForeignKey(user,on_delete=models.CASCADE())
    create_date=models.DateTimeField()
    published_date=models.DateTimeField(default=timezone.now)