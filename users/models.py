from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username,  password=None,is_teacher=False, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),

        )
        user.username = username
        user.is_teacher = is_teacher
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username,  password,  is_teacher=False, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username,
            password,
            **extra_fields
        )
        user.username = username
        user.is_teacher = is_teacher
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_teacher = models.BooleanField(default=False)
    objects = UserManager()