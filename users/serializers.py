from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def validate(self, attrs):
        if attrs['password'] != ['password2']:
            raise ValidationError('Password and password 2 do not math')
        return super().validate(attrs)

    def create(self, validated_data):
        # User.objects.create_user(
        #     username=validated_data['username'],
        #     email=validated_data['email'],
        #     password=validated_data['password'],
        #     first_name=validated_data['first_name'],
        #     last_name=validated_data['last_name'],
        # )
        validated_data('password2')
        return User.objects.create_user(**validated_data)