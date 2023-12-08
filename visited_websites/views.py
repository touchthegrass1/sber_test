from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.response import Response

import uuid

from .models import VisitedLinks
from .serializers import LinksSerializer


@api_view(['POST'])
def save_visited_links(request: Request):
    device_id = request.query_params.get("device_id")
    if device_id is None:
        device_id = uuid.uuid4()

    data = JSONParser().parse(request)
    body = [{"device_id": str(device_id), "link": link} for link in data["links"]]

    serializer = LinksSerializer(data=body, many=True)
    if serializer.is_valid():
        serializer.save()

    response = Response({"status": "ok"})
    response.set_cookie("device_id", device_id)
    return response


@api_view(['GET'])
def get_visited_domains(request: Request):
    device_id = request.COOKIES.get("device_id")
    if device_id is None:
        return Response({"status": "unknown user"}, status=401)

    from_ = float(request.query_params.get('from'))
    to = float(request.query_params.get('to'))
    if from_ is None or to is None:
        return Response({"status": "from or to query parameters not set"})

    from_ = datetime.fromtimestamp(from_)
    to = datetime.fromtimestamp(to)

    visited_domains = VisitedLinks.get_visited_domains(device_id, from_, to)
    return Response({"status": "ok", "domains": visited_domains})
