from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .utils import create_user, update_user

import logging

logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        try:
            user = create_user(**validated_data)
            return user, ""

        except Exception as err:
            logger.error('UserSerializer.create@Error')
            logger.error(err)
            return None, str(err)

    def update(self, instance, validated_data):
        try:
            return update_user(instance, validated_data), ""

        except Exception as err:
            logger.error('UserSerializer.update@Error')
            logger.error(err)
            return None, str(err)

    def validate(self, attrs):
        email = attrs['email']
        if User.objects.exclude(email__iexact=email).filter(email=email).exists():
            return serializers.ValidationError('Email already exists.')
        return attrs


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        print(user)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Invalid Credentials.')
