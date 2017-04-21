import django_filters.rest_framework
from django.utils.dateparse import parse_datetime
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import BoxSerializer, ActivitySerializer, WeightSerializer, RFIDSerializer, ItemSerializer, \
    UserSerializer
from ..models import Box, Activity, RFID, Item, User, Weight


class BaseViewSet(GenericViewSet, RetrieveModelMixin):
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)


class DateFilterable(BaseViewSet):
    # TODO this is done wrong but it works
    # how it should be done!!! /?newer_than=2017-03-28T17:21:02.135853Z
    # http://www.django-rest-framework.org/api-guide/filtering/#specifying-a-filterset
    def get_queryset(self):
        created_raw = self.request.query_params.get('newer_than', None)
        if created_raw:
            created = parse_datetime(created_raw)
            queryset = self.model.objects.filter(created__gt=created)
            print("\n\n\n")
            print(created)
            print("\n\n\n")
        else:
            queryset = self.model.objects.all()

        return queryset


class BoxViewSet(BaseViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    lookup_field = "name"


class ItemViewSet(BaseViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UserViewSet(BaseViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityViewSet(DateFilterable, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    model = Activity
    serializer_class = ActivitySerializer


class RFIDViewSet(DateFilterable, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    model = RFID
    serializer_class = RFIDSerializer


class WeightViewSet(DateFilterable, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    model = Weight
    serializer_class = WeightSerializer
