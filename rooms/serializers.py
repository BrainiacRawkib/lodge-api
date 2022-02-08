from rest_framework import serializers
from .models import Block, Room
from .utils import create_room_block, create_room, update_room

import logging

logger = logging.getLogger(__name__)


class BlockSerializer(serializers.ModelSerializer):
    rooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Block
        fields = ['name', 'total_rooms', 'rooms']

    def create(self, validated_data):
        try:
            return create_room_block(
                validated_data['name'],
                validated_data['total_rooms']
            ), ""

        except Exception as err:
            logger.error('BlockSerializer.create@Error')
            logger.error(err)
            return None, str(err)

    def update(self, instance, validated_data):
        try:
            instance.total_rooms = validated_data.get('total_rooms', instance.total_rooms)
            instance.save()
            return instance, ""

        except Exception as err:
            logger.error('BlockSerializer.update@Error')
            logger.error(err)
            return None, str(err)


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id', 'code', 'room_block', 'room_no', 'available', 'users', 'total_occupants']
        depth = 1
        read_only_fields = ['code', 'room_block', 'users']

    def create(self, validated_data):
        try:
            return create_room(
                validated_data['room_block'], validated_data['room_no'],
                validated_data['total_occupants']
            ), ""

        except Exception as err:
            logger.error('RoomSerializer.create@Error')
            logger.error(err)
            return None, str(err)

    def update(self, instance, validated_data, user):
        try:
            return update_room(instance, user, validated_data), ""

        except Exception as err:
            logger.error("RoomSerializer.update@Error")
            logger.error(err)
            return None, str(err)
