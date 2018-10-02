from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class Quiz(models.Model):
    question = models.TextField(max_length=200,default="")
    option1 = models.CharField(max_length=200,default="")
    option2 = models.CharField(max_length=200, default="")
    option3 = models.CharField(max_length=200, default="")
    option4 = models.CharField(max_length=200, default="")
    answer = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.question

class Guest(models.Model):
    firstname = models.CharField(max_length=200,default="")
    lastname = models.CharField(max_length=200,default="")
    contactnumber = models.CharField(max_length=200,default="")
    score = 1
    def __str__(self):
        return self.firstname

