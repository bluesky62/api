from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .models import msgModel, messagemodel
from .serializers import msgSerializer, messageSerializer


class msgViewset(viewsets.ModelViewSet):
    queryset = msgModel.objects.all()
    serializer_class = msgSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


class messageviewSet(viewsets.ModelViewSet):
    queryset = messagemodel.objects.all()
    serializer_class = messageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
