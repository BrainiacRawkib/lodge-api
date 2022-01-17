from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .utils import *


class RoomAPI(APIView):

    def get(self, request, id=None, format=None):
        pass

    def post(self, request, format=None):
        pass

    def put(self, request, id=None, format=None):
        pass

    def delete(self, request, id=None, format=None):
        pass
