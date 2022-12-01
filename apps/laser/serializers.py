from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Clients, Photos, Sessions, Tatto


class ClientsModelSerializer(ModelSerializer):

    class Meta:
        model = Clients
        fields = "__all__"


class TattoModelSerializer(HyperlinkedModelSerializer):
    client = ClientsModelSerializer

    class Meta:
        model = Tatto
        fields = "__all__"


class SessionsModelSerializer(HyperlinkedModelSerializer):
    client = ClientsModelSerializer

    class Meta:
        model = Sessions
        fields = "__all__"


class PhotosModelSerializer(HyperlinkedModelSerializer):
    tatto = TattoModelSerializer
    session = SessionsodelSerializer

    class Meta:
        model = Photos
        fields = "__all__"