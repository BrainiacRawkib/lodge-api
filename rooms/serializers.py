from rest_framework import serializers
from .models import Block, Room
from .utils import create_room_block, create_room

import logging

logger = logging.getLogger(__name__)


class BlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Block
        fields = '__all__'

    def create(self, validated_data):
        try:
            create_room_block(
                validated_data['name'],
                validated_data['total_rooms']
            )

        except Exception as err:
            logger.error('BlockSerializer.create@Error')
            logger.error(err)
            return None, str(err)

    def update(self, instance, validated_data):
        pass


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ['code']

    def create(self, validated_data):
        try:
            create_room(
                validated_data['room_block'],
                validated_data['room_no']
            )

        except Exception as err:
            logger.error('RoomSerializer.create@Error')
            logger.error(err)
            return None, str(err)

    def update(self, instance, validated_data):
        pass
