from rest_framework import serializers
from reviews.models import (
    Category,
    Genre,
    Title,
)


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre


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
        model = Title
