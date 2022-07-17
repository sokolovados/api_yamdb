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


# class TitleSerializer(serializers.ModelSerializer):
#     category = CategoryTitle(
#         slug_field='slug',
#         queryset=Category.objects.all(),
#         required=False
#     )
#     genre = GenreTitle(
#         slug_field='slug',
#         queryset=Genre.objects.all(),
#         many=True
#     )
#     rating = serializers.IntegerField(
#         source='reviews__score__avg',
#         read_only=True
#     )
#
#     class Meta:
#         model = Title
#         fields = '__all__'
