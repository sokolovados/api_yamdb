from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from django_filters.rest_framework import DjangoFilterBackend

from api.Categories_Genres_Titles.serealizers import *

from reviews.models import Category, Genre, Title

from permissions import AuthorOrReadOnly

from filters import TitlesFilter


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [AuthorOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ["name"]
    lookup_field = "slug"


class GenresViewSet(viewsets.ModelViewSet):
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
