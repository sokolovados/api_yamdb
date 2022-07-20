from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model): #V
    name = models.CharField(
        'name',
        max_length=200,
    )

    slug = models.SlugField(
        'slug',
        unique=True
    )


class Genre(models.Model): #V
    name = models.CharField(
        'name',
        max_length=200,
    )

    slug = models.SlugField(
        'slug',
        unique=True
    )


class Title(models.Model): #V
    name = models.CharField(
        'name',
        max_length=200,
    )

    year = models.IntegerField(
        'year',
        null=True,
        blank=True,
    )

    rating = models.IntegerField(
        default=None,
        null=True,
        blank=True
    )

    description = models.CharField(
        'description',
        null=True,
        blank=True,
        max_length=200,
    )

    genre = models.ManyToManyField(
        Genre,
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='titles'
    )

