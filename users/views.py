from apiutils.views import http_response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from .utils import *


class UserAPI(APIView):
    def get(self, request, *args, **kwargs):
        users = get_all_users()
        serializer = UserSerializer(users, many=True)
        return http_response(
            'User Retrieved',
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass
