from rest_framework import serializers

from reviews.models import (
    Category,
    Genre,
    Title,
)


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "slug",
        )
        model = Category


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "slug",
        )
        model = Genre


class TitlesGetSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(
        read_only=True
    )

    genre = GenresSerializer(
        read_only=True,
        many=True
    )

    rating = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Title


class TitlesPostSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field="slug",
        many=True,
    )

    rating = serializers.IntegerField(
        read_only=True
    )

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field="slug",
    )

    class Meta:
        fields = "__all__"
        model = Title
