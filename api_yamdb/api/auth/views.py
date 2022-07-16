import http
import secrets
import logging

from django.core.mail import send_mail
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.models import User
from rest_framework import mixins, viewsets, status
from .serializers import UserSerializer, UserConfirmSerializer
from rest_framework_simplejwt.tokens import RefreshToken

logger = logging.getLogger(__name__)



class SignUpView(ModelViewSet):

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """
        Gets a username and email,
        creates a user and a confirmation token.
        Sends a token to an email.
        :param request: username and email
        :return: Response
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            confirmation_code = secrets.token_hex(32)
            User.objects.create_user(
                **request.data,
                confirmation_code=confirmation_code
            )
            send_mail(
                subject='YAmdb email confirmation',
                message=f"This is your confirm code: '{confirmation_code}'",
                from_email="yamdb@.test.ru",
                recipient_list=[request.data['email']]
            )
            return Response(request.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['post'])
    def token(self, request):
        """
        Generates and returns a  jwt token
        :param request:
        :return:
        """
        serializer = UserConfirmSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(username=request.data['username'])
            token = RefreshToken.for_user(user)
            return Response(str(token.access_token))

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
