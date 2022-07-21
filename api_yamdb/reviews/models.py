from django.contrib.auth import get_user_model
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


# from users.models import User

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

class Review(models.Model):
    text = models.TextField(
        verbose_name='Текст',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор публикации',
    )
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1),
        ],
        verbose_name='Оценка',
    )

    class Meta:
        ordering = (
            '-pub_date',
        )


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарий',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пользователь',
    )
    text = models.TextField(
        verbose_name='Текст комментария',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата комментария',
    )

    class Meta:
        ordering = (
            '-pub_date',
        )
