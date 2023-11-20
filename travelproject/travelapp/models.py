from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='team')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Front(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='front')

    def __str__(self):
        return self.name
