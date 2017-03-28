import django_filters.rest_framework
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .serializers import BoxSerializer, ActivitySerializer, RFIDSerializer, ItemSerializer, UserSerializer
from ..models import Box, Activity, RFID, Item, User


class BaseViewSet(GenericViewSet, RetrieveModelMixin):
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class BoxViewSet(BaseViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    lookup_field = "name"


class ActivityViewSet(BaseViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class RFIDViewSet(BaseViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    queryset = RFID.objects.all()
    serializer_class = RFIDSerializer

class ItemViewSet(BaseViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UserViewSet(BaseViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
