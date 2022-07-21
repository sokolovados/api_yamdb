from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import validators

from users.models import User


class SelfUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email')
        model = User

    def validate_username(self, value):
        """
        Checks if the username is not 'me'.
        """
        if value == 'me':
            raise validators.ValidationError('Username cannot be "me"')
        return value


class UserConfirmSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=256)
    confirmation_code = serializers.CharField(max_length=256)

    def validate(self, attrs):
        """
        Checks the correctness of the confirmation code.
        :param attrs:
        :return: attrs:
        """
        username = attrs['username']
        confirmation_code = attrs['confirmation_code']
        user = get_object_or_404(User, username=username)
        if user.confirmation_code != confirmation_code:
            raise validators.ValidationError("Invalid confirmation token")
        return attrs


class UserSerializerPrivelege(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
        model = User


class UserSerializerUnprivelege(serializers.ModelSerializer):

    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
        read_only_fields = ('role',)
        model = User
