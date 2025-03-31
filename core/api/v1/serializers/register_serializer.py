from rest_framework import serializers
from identity.models.identity_model import IdentityModel


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6, max_length=12)

    class Meta:
        model = IdentityModel
        fields = ["username", "password"]

    def create(self, validated_data: dict) -> IdentityModel:
        user = IdentityModel.objects.create_user(
            email=validated_data.get("username"),
            username=validated_data.get("username"),
            password=validated_data.get("password")
        )
        return user
    