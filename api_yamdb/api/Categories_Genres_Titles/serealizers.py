from rest_framework import serializers

from reviews.models import (
    Categories,
    Genres,
    Titles,
)


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Categories


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genres


class TitlesSerializer(serializers.ModelSerializer):
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
        model = Titles
