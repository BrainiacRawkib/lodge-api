import string
import random
from .models import Block, Room


# generate
def generate_room_code():
    length = 10
    while True:
        code = ''.join(random.choices(string.ascii_letters, k=length))
        if Room.objects.filter(code=code).exists():
            # if True, generate another code
            generate_room_code()
        else:
            # if False, stop.
            break
    return code


# create
def create_block():
    pass


def create_room():
    pass


# get
def get_room(room_code):
    pass
