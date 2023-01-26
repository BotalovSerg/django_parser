import os
from django.db import models

# path = os.path.abspath('base')


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Choice(models.Model):
    name = models.CharField(max_length=100)
    link = models.FileField(upload_to='base/')
    f_key = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Name {self.name}"
