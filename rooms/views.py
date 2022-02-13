from apiutils.views import http_response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import BlockSerializer, RoomSerializer
from .utils import *


class BlockAPI(APIView):
    lookup_url_kwarg = 'id'

    def get(self, request, format=None):
        token = request.headers.get('Authorization')
        if not token:
            return http_response(
                'Bad Request. Access Token missing.',
                status=status.HTTP_400_BAD_REQUEST
            )

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
        token = request.headers.get('Authorization')
        if not token:
            return http_response(
                'Bad Request. Access Token missing.',
                status=status.HTTP_400_BAD_REQUEST
            )

        payload = request.data
        serializer = BlockSerializer(data=payload)
        if serializer.is_valid():
            data = serializer.validated_data
            created_block, _ = serializer.create(data)
            if created_block:
                return http_response(
                    'Room Block created',
                    status=status.HTTP_201_CREATED,
                    data=data
                )
        return http_response(
            'Bad Request or Room already exists',
            status=status.HTTP_400_BAD_REQUEST,
            data=payload
        )

    def put(self, request, format=None):
        pass

    def delete(self, request, format=None):
        token = request.headers.get('Authorization')
        if not token:
            return http_response(
                'Bad Request. Access Token missing.',
                status=status.HTTP_400_BAD_REQUEST
            )

        query_params = self.request.query_params
        if query_params:
            block_id = query_params.get(self.lookup_url_kwarg)
            if block_id:
                room_block = get_room_block(block_id)
                if room_block:
                    room_block_to_delete = delete_room_block(room_block.id)
                    if room_block_to_delete:
                        return http_response(
                            'Room Block deleted.',
                            status=status.HTTP_204_NO_CONTENT,
                        )
                return http_response(
                    'Room Block not found or already deleted.',
                    status=status.HTTP_404_NOT_FOUND,
                )
        return http_response(
            'No Room Block id passed in params.',
            status=status.HTTP_400_BAD_REQUEST,
        )


class RoomAPI(APIView):
    lookup_url_kwarg = 'code'

    def get(self, request, format=None):
        token = request.headers.get('Authorization')
        if not token:
            return http_response(
                'Bad Request. Access Token missing.',
                status=status.HTTP_400_BAD_REQUEST
            )

        rooms = get_all_rooms()
        serializer = RoomSerializer(rooms, many=True)
        query_params = self.request.query_params
        if query_params:
            code = query_params.get(self.lookup_url_kwarg)
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
        token = request.headers.get('Authorization')
        if not token:
            return http_response(
                'Bad Request. Access Token missing.',
                status=status.HTTP_400_BAD_REQUEST
            )

        payload = request.data
        serializer = RoomSerializer(data=payload)

        if serializer.is_valid():
            data = serializer.validated_data
            data['room_block'] = get_room_block(payload['room_block'])
            created_room, _ = serializer.create(data)
            if created_room:
                return http_response(
                    'Room created',
                    status=status.HTTP_201_CREATED,
                    data=serializer.data
                )
            return http_response(
                'Room number already exist in the room block',
                status=status.HTTP_208_ALREADY_REPORTED,
                data=serializer.data
            )
        return http_response(
            'Bad Request',
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )

    def put(self, request, format=None):
        token = request.headers.get('Authorization')
        if not token:
            return http_response(
                'Bad Request. Access Token missing.',
                status=status.HTTP_400_BAD_REQUEST
            )

        user = get_user_by_token(token)
        query_params = request.query_params
        payload = request.data

        if query_params:
            room_code = query_params.get(self.lookup_url_kwarg)
            room = get_room(room_code)
            payload['room_no'] = room.room_no
            payload['total_occupants'] = room.total_occupants

            if room:
                serializer = RoomSerializer(data=payload)

                if serializer.is_valid():
                    data = serializer.validated_data

                    if not room.available:
                        return http_response(
                            'Cannot add user to room. Room is full',
                            status=status.HTTP_204_NO_CONTENT,
                            data=serializer.data
                        )

                    room_to_update, _ = serializer.update(room, data, user)
                    if room_to_update:
                        return http_response(
                            'User added to room.',
                            status=status.HTTP_200_OK,
                            data=serializer.data
                        )

                    return http_response(
                        'Error adding user to room.',
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data=serializer.errors
                    )
            return http_response(
                'Room not found',
                status=status.HTTP_404_NOT_FOUND,
                data=payload
            )
        return http_response(
            'No params given for lookup',
            status=status.HTTP_400_BAD_REQUEST,
            data=payload
        )

    def delete(self, request, format=None):
        token = request.headers.get('Authorization')
        if not token:
            return http_response(
                'Bad Request. Access Token missing.',
                status=status.HTTP_400_BAD_REQUEST
            )

        query_params = request.query_params
        if query_params:
            code = query_params.get(self.lookup_url_kwarg)
            if code:
                room = get_room(code)
                if room:
                    room_to_delete = delete_room(room.code)

                    if room_to_delete:
                        return http_response(
                            'Room deleted.',
                            status=status.HTTP_204_NO_CONTENT,
                        )
                return http_response(
                    'Room not found or already deleted.',
                    status=status.HTTP_404_NOT_FOUND,
                )
        return http_response(
            'No room code found.',
            status=status.HTTP_400_BAD_REQUEST
        )
