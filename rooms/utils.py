import string
import random
from .models import Block, Room

import logging

logger = logging.getLogger(__name__)


# GENERATE ROOM CODE
def generate_room_code():
    """Generate unique code for rooms."""
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


# CREATE MODELS
def create_room_block(name, total_rooms):
    """Create Block (Block A, Block B, e.t.c) for Rooms."""
    try:
        if Block.objects.filter(name=name).exists():
            return None
        return Block.objects.create(name=name, total_rooms=total_rooms)

    except Exception as e:
        logger.error('create_room_block@Error')
        logger.error(e)
        return None


def create_room(**kwargs):
    """Create Room."""
    try:
        # if Room.objects.filter(room_block=room_block, room_no=room_no).exists():
        #     return None
        # room = Room.objects.create(
        #     code=generate_room_code(),
        #     room_block=room_block,
        #     room_no=room_no,
        # )
        room = Room.objects.create(
            code=generate_room_code(),
            room_block=kwargs['room_block'],
            room_no=kwargs['room_no'],
        )
        return room.pk

    except Exception as e:
        logger.error('create_room@Error')
        logger.error(e)
        return None


# GET MODELS
def get_room(room_code):
    """Get room."""
    try:
        return Room.objects.get(code=room_code)

    except Exception as e:
        logger.error('get_room@Error')
        logger.error(e)
        return None


def get_all_rooms():
    """Get all rooms."""
    try:
        return Room.objects.all()

    except Exception as e:
        logger.error('get_all_rooms@Error')
        logger.error(e)
        return []


def get_room_block(block_id):
    """Get a Room Block."""
    try:
        return Block.objects.get(id=block_id)

    except Exception as e:
        logger.error('get_room_block@Error')
        logger.error(e)
        return None


def get_all_room_blocks():
    """Get all Room Blocks."""
    try:
        return Block.objects.all()

    except Exception as e:
        logger.error('get_all_room_blocks@Error')
        logger.error(e)
        return []


# DELETE MODELS
def delete_room_block(block_id):
    """Delete Room Block by id."""
    try:
        Block.objects.get(id=block_id).delete()
        return True

    except Exception as e:
        logger.error("delete_room_block@Error")
        logger.error(e)
        return None


def delete_room(room_code):
    """Delete Room by id."""
    try:
        Room.objects.get(code=room_code).delete()
        return True

    except Exception as e:
        logger.error("delete_room@Error")
        logger.error(e)
        return None
