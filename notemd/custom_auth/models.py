from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        app_label = 'custom_auth'

    