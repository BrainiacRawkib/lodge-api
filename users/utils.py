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


def get_user_by_token(token):
    try:
        key = token.split()
        access_token = key[1]
        token = Token.objects.get(key=access_token)
        user = token.user
        if user and user.is_active:
            return user
        return None

    except Exception as e:
        logger.error('get_user_by_token@Error')
        logger.error(e)
        return None

# UPDATE MODELS

def update_user(instance, validated_data):
    try:
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if User.objects.exclude(username=instance.username, email=instance.email)\
                .filter(username=instance.username, email=instance.email).exists():
            return None
        instance.set_password(instance.password)
        instance.save()
        token, created = Token.objects.get_or_create(user=instance)
        return instance, token

    except Exception as e:
        logger.error('update_user@Error')
        logger.error(e)
        return None


def update_user_email(user_email, email):
    try:
        if user_email == email:
            return True
        else:
            if User.objects.filter(email=email).exists():
                return False
            return True

    except Exception as e:
        logger.error('update_user_email@Error')
        logger.error(e)
        return False


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
