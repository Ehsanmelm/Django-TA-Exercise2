from django.db import models
from django.contrib.auth.models import UserManager,AbstractBaseUser , PermissionsMixin
from django.contrib.auth.hashers import make_password
# Create your models here.

class UserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone:
            raise ValueError("The given phone must be set")
        phone = self.normalize_email(phone)

        user = self.model(phone =phone , **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self ,phone =None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self,phone =None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone, password, **extra_fields)

class User(AbstractBaseUser , PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(unique=True,max_length=11)
    is_staff = models.BooleanField(blank=True , null=True)

    objects = UserManager();
    USERNAME_FIELD = 'phone';