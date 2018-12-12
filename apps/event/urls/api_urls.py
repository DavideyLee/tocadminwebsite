# coding:utf-8

from rest_framework_bulk.routes import BulkRouter
from .. import api

app_name = 'appi-events'

router = BulkRouter()
router.register(r'events', api.EventViewSet, 'event')

urlpatterns = [
    # path('assets-bulk/', api.AssetListUpdateApi.as_view(), name='asset-bulk-update'),
]

urlpatterns += router.urls
