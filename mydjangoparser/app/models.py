import os
from django.conf import settings
from django.db import models


def path_dir():
    return os.path.join(settings.LOCAL_FILE_DIR, 'base')


class Choice(models.Model):
    name = models.CharField(max_length=100)
    link = models.FilePathField(path='mydjangoparser/base')

    def __str__(self):
        return f"Name {self.name}"
