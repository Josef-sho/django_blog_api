from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models

class CustomUser(AbstractUser):
    # Custom fields and methods go here

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=('The groups this user belongs to.'),
        related_query_name='customuser'  # Use related_query_name instead of related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='customuser'  # Use related_query_name instead of related_name
    )