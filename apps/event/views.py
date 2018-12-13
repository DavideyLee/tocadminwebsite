# ~*~ coding: utf-8 ~*~

from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin

from common.utils import get_logger
from common.const import create_success_msg, update_success_msg
from common.permissions import AdminUserRequiredMixin
from orgs.utils import current_org
from .models import Event
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

__all__ = ['EventListView']
logger = get_logger(__name__)


class EventListView(AdminUserRequiredMixin, TemplateView):
    template_name = 'event/event_list.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Event'),
            'action': _('Event list')
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class EventCreateView(AdminUserRequiredMixin, SuccessMessageMixin, CreateView):
    model = Event
    form_class = forms.EventCreateUpdateForm
    template_name = 'event/event_create.html'
    success_url = reverse_lazy('events:event-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        return form

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Event'),
            'action': _('Create event'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)

    def get_success_message(self, cleaned_data):
        return create_success_msg % ({"name": cleaned_data["title"]})


class EventUpdateView(AdminUserRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Event
    form_class = forms.EventCreateUpdateForm
    template_name = 'event/event_update.html'
    success_url = reverse_lazy('events:event-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        return form

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Event'),
            'action': _('Update event'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)

    def get_success_message(self, cleaned_data):
        return create_success_msg % ({"name": cleaned_data["title"]})

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'event/event_detail.html'

    def get_context_data(self, **kwargs):
        events_remain = Node.objects.exclude(assets=self.object)
        context = {
            'app': _('Event'),
            'action': _('Event detail'),
            'events_remain': events_remain,
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)