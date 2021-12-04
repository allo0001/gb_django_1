from django.contrib.auth.models import AbstractUser
from django.db import models

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users', blank=True)
    age = models.SmallIntegerField(default=18, verbose_name='Возраст')
