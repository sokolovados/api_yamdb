from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.Categories_Genres_Titles.views import (
    CategoriesViewSet,
    GenresViewSet,
    TitlesViewSet,
)

app_name = 'api'

router = DefaultRouter()

router.register(
    'titles',
    TitlesViewSet,
    basename='titles'
)

router.register(
    'genres',
    GenresViewSet,
    basename='genres'
)

router.register(
    'categories',
    CategoriesViewSet,
    basename='categories'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
