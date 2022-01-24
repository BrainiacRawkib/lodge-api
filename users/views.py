from apiutils.views import http_response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer


class UserAPI(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            return http_response(
                'User Retrieved',
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        return http_response(
            'Error Retrieving User',
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.data
        )

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass
