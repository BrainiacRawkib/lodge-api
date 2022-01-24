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
def get_user(**kwargs):
    try:
        user = User.objects.get(kwargs)
        return user

    except Exception as e:
        logger.error('get_user@Error')
        logger.error(e)
        return None
