from django.db import models

# Create your models here.


class Station_search(models.Model):
    words = models.CharField(max_length=30)