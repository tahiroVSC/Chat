from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.chats.models import Message,Rooms
from apps.chats.serializers import RoomSerializer,BackMessageSerializer,FrontMessageSerializer,UXUIMessageSerializer,AndroidMessageSerializer

class BackListViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = BackMessageSerializer

class RoomsListViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer

class FrontListViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = FrontMessageSerializer

class UxUiListViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = UXUIMessageSerializer

class AndroidListViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = AndroidMessageSerializer




