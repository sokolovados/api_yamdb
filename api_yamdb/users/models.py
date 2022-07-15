from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    # User role choices.
    ADMIN = 'admin'
    USER = 'user'
    MODERATOR = 'moderator'
    USER_ROLES = (
        (ADMIN, 'admin'),
        (USER, 'user'),
        (MODERATOR, 'moderator'),
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        max_length=256, choices=USER_ROLES,
        default=USER
    )