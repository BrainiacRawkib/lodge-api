from rest_framework import serializers
from django.contrib.auth.models import User
from .utils import create_user

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
