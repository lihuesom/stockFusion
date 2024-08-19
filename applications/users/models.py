from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        primary_key=True,
        error_messages={
            'unique': 'Ya existe un usuario con ese correo.'
        }
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cellphone = models.BigIntegerField(
        default=0,
        error_messages={
            'unique': 'Ya existe un usuario con ese teléfono.'
        }
    )
    identification = models.CharField(
        max_length=50,
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con esa identificación.'
        }
    )
    document_type = models.CharField(
        max_length=50,
        choices=[
            ('CC', 'Cédula de Ciudadanía'),
            ('TI', 'Tarjeta de Identidad'),
            ('PAS', 'Pasaporte'),
            ('NIT', 'Número de Identificación Tributaria'),
        ]
    )

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name='custom_user_groups'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_user_permissions'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'cellphone', 'identification', 'document_type']

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
