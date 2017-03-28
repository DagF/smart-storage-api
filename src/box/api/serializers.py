from rest_framework.serializers import ModelSerializer, SlugRelatedField

from ..models import Box, RFID, Activity, Item, User, Weight


class BoxSerializer(ModelSerializer):
    url_path = "box"

    class Meta(object):
        model = Box
        fields = (
            'uuid',
            'name',
        )


class RFIDSerializer(ModelSerializer):
    url_path = "rfid"
    box = SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='name',
        queryset=Box.objects.all()
    )

    class Meta(object):
        model = RFID
        fields = (
            'uuid',
            'box',
            'value',
            'created',
        )


class ActivitySerializer(ModelSerializer):
    url_path = "activities"
    box = SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='name',
        queryset=Box.objects.all()
    )

    class Meta(object):
        model = Activity
        fields = (
            'uuid',
            'box',
            'created',
        )


class ItemSerializer(ModelSerializer):
    url_path = "items"

    class Meta(object):
        model = Item
        fields = (
            'uuid',
            'name',
            'description',
            'created',
            'weight',
            'full_weight',
            'empty_weight',
            'type',
        )


class UserSerializer(ModelSerializer):
    url_path = "users"

    class Meta(object):
        model = User
        fields = (
            'uuid',
            'name',
            'rfid',
            'created',
        )


class WeightSerializer(ModelSerializer):
    url_path = "weight"
    box = SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='name',
        queryset=Box.objects.all()
    )

    class Meta(object):
        model = Weight
        fields = (
            'uuid',
            'box',
            'created',
            'value',
        )
