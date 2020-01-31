from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """
        Create a new user profile.

        :param email: A string of email address.
        :param name: A string of user's name.
        :param password: A string of password. Can be None by default.
        :return: A user model.
        """
        if not email:
            raise ValueError('Users much have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        Create a superuser profile.

        :param email: A string of email address.
        :param name: A string of user's name.
        :param password: A string of password.
        :return: A user model.
        """
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user."""
        return self.name

    def get_short_name(self):
        """Retrieve a short name of user."""
        return self.name

    def __str__(self):
        """Return string representation of user."""
        return self.email
