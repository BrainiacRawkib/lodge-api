import string
import random
from .models import Block, Room

import logging

logger = logging.getLogger(__name__)


# generate
def generate_room_code():
    try:
        length = 10
        while True:
            code = ''.join(random.choices(string.ascii_letters, k=length))
            if Room.objects.filter(code=code).exists():
                # if True, generate another code
                generate_room_code()

            else:
                # if False, stop.
                break
        return f'ROOM_{code}'

    except Exception as e:
        logger.error('generate_room_code@Error')
        logger.error(e)
        return None


# create
def create_room_block(name, total_rooms):
    try:
        return Block.objects.create(name=name, total_rooms=total_rooms)

    except Exception as e:
        logger.error('create_room_block@Error')
        logger.error(e)
        return None


def create_room(room_block, room_no):
    try:
        return Room.objects.create(
            code=generate_room_code(),
            room_block=room_block,
            room_no=room_no,
        )

    except Exception as e:
        logger.error('create_room@Error')
        logger.error(e)
        return None


# get
def get_room(room_code):
    pass
