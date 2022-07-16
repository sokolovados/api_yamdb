from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .auth.views import SignUpView

router_v1 = DefaultRouter()
router_v1.register(r'auth', SignUpView, basename='auth')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
