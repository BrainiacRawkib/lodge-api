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
        query_params = self.request.query_params
        if query_params:
            room_block_id = query_params['id']
            if room_block_id:
                room_block = get_room_block(room_block_id)
                serializer = BlockSerializer(room_block)
                return http_response(
                    'Room Block retrieved',
                    status=status.HTTP_200_OK,
                    data=serializer.data
                )
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
                    'Room Block created',
                    status=status.HTTP_201_CREATED,
                    data=data
                )
        return http_response(
            'Bad Request',
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, id=None, format=None):
        pass

    def delete(self, request, id=None, format=None):
        room_block = get_room_block(id)
        room_block_to_delete = delete_room_block(room_block.id)
        if not room_block_to_delete:
            return http_response(
                'Room Block not found.',
                status=status.HTTP_404_NOT_FOUND,
            )
        return http_response(
            'Room Block deleted.',
            status=status.HTTP_204_NO_CONTENT,
        )


class RoomAPI(APIView):
    lookup_url_kwarg = 'code'

    def get(self, request, format=None):
        rooms = get_all_rooms()
        serializer = RoomSerializer(rooms, many=True)
        query_params = self.request.query_params
        if query_params:
            code = query_params['code']
            if code:
                room = get_room(code)
                serializer = RoomSerializer(room)
                return http_response(
                    'Room retrieved',
                    status=status.HTTP_200_OK,
                    data=serializer.data
                )
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
            if created_room:
                return http_response(
                    'Room created',
                    status=status.HTTP_201_CREATED,
                    data=data
                )
        return http_response(
            'Bad Request',
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, id=None, format=None):
        pass

    def delete(self, request, format=None):
        room = get_room(self.lookup_url_kwarg)
        room_to_delete = delete_room(room.code)

        if not room_to_delete:
            return http_response(
                'Room not found.',
                status=status.HTTP_404_NOT_FOUND,
            )
        return http_response(
            'Room deleted.',
            status=status.HTTP_204_NO_CONTENT,
        )
