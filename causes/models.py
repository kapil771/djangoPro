from django.db import models

# Create your models here.
class Causes(models.Model):
    image=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField()