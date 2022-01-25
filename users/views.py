from apiutils.views import http_response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from .utils import *


class UserAPI(APIView):
    def get(self, request, *args, **kwargs):
        users = get_all_users()
        serializer = UserSerializer(users, many=True)
        query_params = request.query_params
        if query_params:
            username = query_params['username']
            if username:
                user = get_user(username)
                if user:
                    serializer = UserSerializer(user)
                    return http_response(
                        'User Retrieved',
                        status=status.HTTP_200_OK,
                        data=serializer.data
                    )
                return http_response(
                    'User not found',
                    status=status.HTTP_404_NOT_FOUND,
                )
        return http_response(
            'Users Retrieved',
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
        query_params = request.query_params
        payload = request.data
        if query_params:
            user = query_params['username']
            if user:
                serializer = UserSerializer(data=payload)
                if serializer.is_valid():
                    data = serializer.validated_data
                    user_to_update, _ = serializer.update(user, data)
                    if user_to_update:
                        return http_response(
                            'User updated.',
                            status=status.HTTP_200_OK,
                            data=serializer.data
                        )
                    return http_response(
                        'Server Error',
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data=serializer.errors
                    )
            return http_response(
                'Bad Request. Specify a user to update',
                status=status.HTTP_400_BAD_REQUEST
            )
        return http_response(
            'Bad Request.',
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, *args, **kwargs):
        query_params = request.query_params
        if query_params:
            user = query_params['username']
            if user:
                user_to_delete = delete_user(user)

                if user_to_delete:
                    return http_response(
                        'User deleted.',
                        status=status.HTTP_204_NO_CONTENT,
                    )
                return http_response(
                    'User not found or already deleted.',
                    status=status.HTTP_404_NOT_FOUND
                )
        return http_response(
            'No username param passed.',
            status=status.HTTP_400_BAD_REQUEST
        )
