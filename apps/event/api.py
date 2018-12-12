# -*- coding: utf-8 -*-
#

from rest_framework_bulk import BulkModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from common.mixins import IDInFilterMixin
from common.utils import get_logger
from .serializers import EventSerializer
from .models import Event
from common.permissions import IsValidUser


logger = get_logger(__file__)
__all__ = [
    'EventViewSet',
]

class EventViewSet(IDInFilterMixin, BulkModelViewSet):
    """
    事件查询或操作的api
    """
    filter_fields = ('title',)
    search_fields = filter_fields
    ordering_fields = ('created_time',)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsValidUser,)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset