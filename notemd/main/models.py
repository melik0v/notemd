from django.db import models


class Note(models.Model):
    title = models.CharField('Title', max_length=255)
    content = models.TextField('Content')
