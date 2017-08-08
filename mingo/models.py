from django.db import models

# Create your models here.
class Sighting(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    data = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    fin_type = models.CharField(max_length=50)
    whale_type = models.CharField(max_length=50)
    blow_type = models.CharField(max_length=50)
    wave_type = models.CharField(max_length=50)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username