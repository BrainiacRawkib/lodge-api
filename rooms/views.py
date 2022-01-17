from apiutils.views import http_response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import BlockSerializer, RoomSerializer
from .utils import *


class BlockAPI(APIView):

    def get(self, request, id=None, format=None):
        room_blocks = get_all_room_blocks()
        serializer = BlockSerializer(room_blocks, many=True)
        return http_response(
            'Room Blocks retrieved',
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def post(self, request, format=None):
        payload = request.data
        serializer = BlockSerializer(data=payload)
        if serializer.is_valid():
            data = serializer.validated_data
            created_block, _ = serializer.create(data)
            if not created_block:
                return http_response(
                    'Server Error',
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return http_response(
                'Room Block created',
                status=status.HTTP_201_CREATED,
                data=data
            )

    def put(self, request, id=None, format=None):
        pass

    def delete(self, request, id=None, format=None):
        pass


class RoomAPI(APIView):

    def get(self, request, id=None, format=None):
        rooms = get_all_rooms()
        serializer = RoomSerializer(rooms, many=True)
        return http_response(
            'Rooms retrieved',
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def post(self, request, format=None):
        payload = request.data
        serializer = RoomSerializer(data=payload)
        if serializer.is_valid():
            data = serializer.validated_data
            created_room, _ = serializer.create(data)
            if not created_room:
                return http_response(
                    'Server Error',
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return http_response(
                'Room created',
                status=status.HTTP_201_CREATED,
                data=data
            )

    def put(self, request, id=None, format=None):
        pass

    def delete(self, request, id=None, format=None):
        pass
