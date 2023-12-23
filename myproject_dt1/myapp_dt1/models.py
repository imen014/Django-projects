from django.db import models

class Bd1(models.Model):
    username = models.CharField(max_length=10)
    job = models.CharField(max_length=20)
