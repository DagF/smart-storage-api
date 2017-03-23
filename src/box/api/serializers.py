from rest_framework.serializers import ModelSerializer, SerializerMethodField, SlugRelatedField, Field

from ..models import Box, RFID, Activity


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




