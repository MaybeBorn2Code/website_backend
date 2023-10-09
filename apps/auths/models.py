# Django
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class ClientManager(BaseUserManager):
    """Manager for create clients."""

    def create_user(
        self,
        email: str,
        username: str,
        first_name: str,
        last_name: str,
        password: str,
    ) -> 'Client':
        """Registration user."""

        if not email:
            raise ValidationError('Email required')

        user: 'Client' = self.model(
            email=self.normalize_email(email),
        )
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email: str,
        username: str,
        password: str,
        first_name: str,
        last_name: str,
    ) -> 'Client':
        """Create admin."""

        user: 'Client' = self.model(
            email=self.normalize_email(email),
        )
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user


class Client(AbstractBaseUser, PermissionsMixin):
    """Model for clients."""

    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name='почта'
    )
    first_name = models.CharField(
        max_length=32,
        verbose_name='имя',
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=32,
        verbose_name='фамилия',
        null=True,
        blank=True
    )
    username = models.CharField(
        max_length=32,
        verbose_name='имя пользователя',
        unique=True
    )
    photo = models.ImageField(
        upload_to='profiles/photo',
        verbose_name='фото профиля',
        null=True,
        blank=True,
    )
    about = models.TextField(
        verbose_name='о себе',
        max_length=300
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='активность'
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name='администратор'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='менеджер'
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name='дата регистрации'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = ClientManager()

    class Meta:
        ordering = (
            '-date_joined',
        )
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self) -> str:
        return f'{self.email} | {self.username} | {self.date_joined}'
    
