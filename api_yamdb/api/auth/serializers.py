from rest_framework import serializers
from rest_framework.validators import ValidationError, UniqueValidator

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email')
        model = User


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
        user = User.objects.get(username=username)
        if user.confirmation_code != confirmation_code:
            raise ValidationError("Invalid confirmation token")
        return attrs
