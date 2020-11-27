from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """ User class abstracted from django user model """

    def __str__(self):
        return self.get_full_name()