from apiutils.views import http_response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import BlockSerializer, RoomSerializer
from .utils import *


class BlockAPI(APIView):

    def get(self, request, id=None, format=None):
        pass

    def post(self, request, format=None):
        pass

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
        pass

    def put(self, request, id=None, format=None):
        pass

    def delete(self, request, id=None, format=None):
        pass
