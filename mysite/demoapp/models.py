from django.db import models

# Create your models here.

class Notification(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=500, blank=False)
    link = models.CharField(max_length=200, blank=True)
    date_added =  models.DateField(auto_now_add=True)
    ntype = models.CharField(max_length=500, blank=False)
    description = models.CharField(max_length=1500, blank=False)