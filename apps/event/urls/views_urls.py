# -*- coding: utf-8 -*-
#

from django.urls import path

from .. import views

app_name = 'event'


urlpatterns = [
    # User event view
    path('event/', views.EventListView.as_view(), name='event-list'),
    # path('event/<uuid:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('event/create/', views.EventCreateView.as_view(), name='event-create'),
    path('event/<uuid:pk>/update/', views.EventUpdateView.as_view(), name='event-update'),
]
