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
        payload = request.data
        serializer = UserSerializer(data=payload)
        if serializer.is_valid():
            data = serializer.validated_data
            created_user, _ = serializer.create(data)
            if created_user:
                return http_response(
                    'User created',
                    status=status.HTTP_201_CREATED,
                    data=serializer.data
                )
            return http_response(
                'Server Error',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data=serializer.data
            )
        return http_response(
            'Bad Request',
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.data
        )

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass
