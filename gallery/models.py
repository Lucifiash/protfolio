from django.db import models

# Create your models here.
class Gallery(models.Model):
    descripiton = models.CharField(max_length=50)