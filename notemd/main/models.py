from django.db import models
from mdeditor.fields import MDTextField


class Note(models.Model):
    title = models.CharField('Title', max_length=255)
    content = MDTextField()

    def __unicode__(self):
        return self.name
