from django.db import models

# Create your models here.
class StudentStats(models.Model):
    hp = models.IntegerField(default=0)
    iq = models.IntegerField(default=0)
    ha = models.IntegerField(default=0)
    date = models.DateTimeField(default=None)