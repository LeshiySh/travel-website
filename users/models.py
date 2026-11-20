import re
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = None
    last_name = None

    full_name = models.CharField('ФИО', max_length=255)
    phone = models.CharField('Телефон', max_length=20)

    @property
    def formatted_phone(self):
        digits = re.sub(r'\D', '', self.phone or '')
        if len(digits) == 11:
            return f"+7({digits[1:4]}){digits[4:7]}-{digits[7:9]}-{digits[9:11]}"
        return self.phone

    def __str__(self):
        return self.username