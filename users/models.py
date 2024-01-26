from django.db import models

from django.contrib.auth.models import AbstractUser

NULLABLE = {
    'null': True,
    'blank': True
}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
