from rest_framework import serializers
from django.contrib.auth.models import User
from .utils import create_user, update_user

import logging

logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

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
            # return update_user(instance, validated_data), ""
            instance.username = validated_data.get('username', instance.username)
            instance.email = validated_data.get('email', instance.email)
            # if User.objects.exclude(username=instance.username) \
            #         .filter(username=instance.username, email=instance.email).exists():
            #     return None
            instance.save()
            return instance, ""

        except Exception as err:
            logger.error('UserSerializer.update@Error')
            logger.error(err)
            return None, str(err)
