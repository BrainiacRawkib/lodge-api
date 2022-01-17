from rest_framework.response import Response


def http_response(msg, status, data=None):
    if data is None:
        data = {}

    response_data = dict(
        msg=msg, data=data
    )

    return Response(response_data, status=status)
