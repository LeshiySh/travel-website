from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = None
    last_name = None

    full_name = models.CharField('ФИО', max_length=255)
    phone = models.CharField('Телефон', max_length=20)

    def __str__(self):
        return self.username