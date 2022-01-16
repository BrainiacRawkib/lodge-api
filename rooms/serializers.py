from rest_framework import serializers
from .models import Block, Room


class BlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Block
        fields = '__all_'


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ['code']
