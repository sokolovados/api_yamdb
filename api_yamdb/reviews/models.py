from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Categories(models.Model):
    name = models.CharField(
        'name',
        max_length=200,
    )

    slug = models.SlugField(
        'slug',
        unique=True
    )


class Genres(models.Model):
    name = models.CharField(
        'name',
        max_length=200,
    )

    slug = models.SlugField(
        'slug',
        unique=True
    )


class Titles(models.Model):
    name = models.CharField(
        'name',
        max_length=200,
    )

    year = models.IntegerField(
        'year',
        null=True,
        blank=True,
    )

    genre = models.ForeignKey(
        Genres,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='genre'
    )

    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='category'
    )

    description = models.CharField(
        'description',
        max_length=200,
        null=True,
    )

    # reviews = models.ForeignKey(
    #     'reviews',
    #     Reviews,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    # )
