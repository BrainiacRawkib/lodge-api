from django.contrib.auth.models import User

import logging

logger = logging.getLogger(__name__)


# CREATE MODELS
def create_user(**kwargs):
    try:
        user = User.objects.create(**kwargs)
        return user

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


def get_user(**kwargs):
    try:
        user = User.objects.get(kwargs)
        return user

    except Exception as e:
        logger.error('get_user@Error')
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
