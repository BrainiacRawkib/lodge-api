from rest_framework import serializers
from .models import Block, Room
from .utils import create_room_block, create_room

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
        fields = ['code', 'room_block', 'room_no', 'available']
        # depth = 1
        read_only_fields = ['code', 'room_block']

    def create(self, validated_data):
        try:
            # room = create_room(
            #         **validated_data
            # )
            room = Room.objects.create(**validated_data)
            return room, ""

        except Exception as err:
            logger.error('RoomSerializer.create@Error')
            logger.error(err)
            return None, str(err)

    def update(self, instance, validated_data):
        try:
            instance.room_block = validated_data.get('room_block', instance.room_block)
            instance.room_no = validated_data.get('room_no', instance.room_no)
            instance.available = validated_data.get('available', instance.available)
            instance.save()
            return instance, ""

        except Exception as err:
            logger.error("RoomSerializer.update@Error")
            logger.error(err)
            return None, str(err)
