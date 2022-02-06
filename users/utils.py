from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

import logging

logger = logging.getLogger(__name__)


# CREATE MODELS
def create_user(**kwargs):
    try:
        if User.objects.filter(email=kwargs['email']).exists():
            return None
        user = User.objects.create_user(**kwargs)
        token, created = Token.objects.get_or_create(user=user)
        return user, token

    except Exception as e:
        logger.error('create_user@Error')
        logger.error(e)
        return None


# GET MODELS
def get_all_users():
    try:
        users = User.objects.all()
        return users

    except Exception as e:
        logger.error('get_all_users@Error')
        logger.error(e)
        return []


def get_user(username):
    try:
        user = User.objects.get(username=username)
        if not user:
            return None
        return user

    except Exception as e:
        logger.error('get_user@Error')
        logger.error(e)
        return None


# UPDATE MODELS

def update_user(instance, validated_data):
    try:
        ins = get_user(instance)
        ins.username = validated_data.get('username', ins.username)
        ins.email = validated_data.get('email', ins.email)
        ins.password = validated_data.get('password', ins.password)
        if User.objects.exclude(username=ins.username, email=ins.email)\
                .filter(username=ins.username, email=ins.email).exists():
            return None
        ins.save()
        return ins

    except Exception as e:
        logger.error('update_user@Error')
        logger.error(e)
        return None


# DELETE USER
def delete_user(user):
    try:
        user = get_user(username=user)
        user.delete()
        return True

    except Exception as e:
        logger.error('delete_user@Error')
        logger.error(e)
        return False
