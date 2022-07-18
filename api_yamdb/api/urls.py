from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .auth.views import SignUpView

from api.Categories_Genres_Titles.views import (
    CategoriesViewSet,
    GenresViewSet,
    TitlesViewSet,
)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'auth', SignUpView, basename='auth')

router_v1.register(
    'titles',
    TitlesViewSet,
    basename='titles'
)

router_v1.register(
    'genres',
    GenresViewSet,
    basename='genres'
)

router_v1.register(
    'categories',
    CategoriesViewSet,
    basename='categories'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
