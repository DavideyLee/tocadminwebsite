# -*- coding: utf-8 -*-
#
from rest_framework import serializers
from rest_framework_bulk.serializers import BulkListSerializer

from common.mixins import BulkSerializerMixin
from ..models import Event


__all__ = [
    'EventSerializer',
]


class EventSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    事件的数据结构
    """
    class Meta:
        model = Event
        list_serializer_class = BulkListSerializer
        fields = '__all__'
        validators = []

    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)
        fields.extend([
            'get_user', 'get_event_level', 'get_event_state'
        ])
        return fields