from django.db import models

# Create your models here.

class Servicio(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    providerurl = models.URLField()

    def __str__(self):
        return self.name

