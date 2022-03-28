from django.db import models

# Create your models here.


class Leads(models.Model):

    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)

    def __str__(self):
        return self.name