from rest_framework.viewsets import ModelViewSet
from .models import Photos, Sessions, Tatto, Clients
from .serializers import PhotosModelSerializer, SessionsModelSerializer, TattoModelSerializer, ClientsModelSerializer


class PhotosModelViewSet(ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotosModelSerializer


class SessionsModelViewSet(ModelViewSet):
    queryset = Sessions.objects.all()
    serializer_class = SessionsModelSerializer


class TattoModelViewSet(ModelViewSet):
    queryset = Tatto.objects.all()
    serializer_class = TattoModelSerializer


class ClientsModelViewSet(ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsModelSerializer
