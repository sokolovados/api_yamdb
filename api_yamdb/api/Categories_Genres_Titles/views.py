from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from django_filters.rest_framework import DjangoFilterBackend

from api.Categories_Genres_Titles.serealizers import *

from reviews.models import Category, Genre, Title

from api.Categories_Genres_Titles.permissions import AuthorOrReadOnly

from api.Categories_Genres_Titles.filters import TitlesFilter


class CategoriesViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [AuthorOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ["name"]
    lookup_field = "slug"


class GenresViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
    permission_classes = [AuthorOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ["name"]
    lookup_field = "slug"


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitlesGetSerializer
    permission_classes = [AuthorOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitlesGetSerializer
        return TitlesPostSerializer
