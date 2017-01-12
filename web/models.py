from django.db import models

# Create your models here.
class Web(models.Model):
    url = models.CharField(max_length=255)
