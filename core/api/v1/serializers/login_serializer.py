from rest_framework import serializers
from django.contrib.auth import authenticate
from identity.models.identity_model import IdentityModel


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data: dict) -> IdentityModel:
        user: IdentityModel = authenticate(
            username=data.get("email"),
            password=data.get("password")
        )
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user
    