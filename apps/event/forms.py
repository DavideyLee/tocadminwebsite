# -*- coding: utf-8 -*-
#
from django import forms
from django.utils.translation import gettext_lazy as _

from common.utils import get_logger
from orgs.mixins import OrgModelForm

from .models import Event


logger = get_logger(__file__)
__all__ = ['EventCreateUpdateForm']


class EventCreateUpdateForm(OrgModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 'finish_time',  'event_starttime',
            'event_endtime', 'system_name', 'event_level', 'event_leader', 'comment',
            'event_cause', 'event_state',
            'solve_event_comment', 'avoid_event_comment',
        ]

        help_texts = {
            'title': '* required',
            'system_name': '* required',
            'event_leader': '* required',
        }
