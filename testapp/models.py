from django.db import models
class tempmodel(models.Model):
        name=models.CharField(max_length=40)
        roll=models.IntegerField()
        city=models.CharField(max_length=30)
        feedbackform=models.CharField(max_length=100)
