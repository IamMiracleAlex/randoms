import uuid

from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from randoms.models import Random
from randoms.serializers import RandomSerializer


class RandomView(APIView):
    '''Gets all uuids
        GET -- /uuids/
    '''

    def get(self, request, *args, **kwargs):
        new_uuid = uuid.uuid4().hex
        now = timezone.now()
        Random.objects.create(uuid=new_uuid, date=now)

        uuids = Random.objects.all()
        serializer = RandomSerializer(uuids, many=True).data
    
        return Response(serializer, status=status.HTTP_200_OK)
