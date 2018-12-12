from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from orgs.mixins import OrgModelMixin
from django.utils import timezone
from users.models import User

# Create your models here.

__all__ = ['Event']


class Event(models.Model):
    EVENT_LEVEL_CHOICES = (
        (1, _('1 LEVEL')),
        (2, _('2 LEVEL')),
        (3, _('3 LEVEL')),
        (4, _('4 LEVEL')),
        (5, _('5 LEVEL')),
        (6, _('6 LEVEL')),
        (7, _('7 LEVEL')),
        (8, _('8 LEVEL')),
    )

    EVENT_STATE_CHOICES = (
        (0, _('STATE 1')),
        (1, _('STATE 2')),
        (2, _('STATE 3')),
        (3, _('STATE 4')),
        (4, _('STATE 5')),
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=70, unique=True, verbose_name=_('Title'))   # 事件标题
    created_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_('Create time'))  # 事件记录创建时间
    modified_time = models.DateTimeField(auto_now=True, verbose_name=_('Modified time'))  # 事件记录最后修改时间
    finish_time = models.DateTimeField(verbose_name=_('Finish time'))  # 事件关闭时间
    event_starttime = models.DateTimeField(verbose_name=_('Event starttime'))  # 事件故障开始时间
    event_endtime = models.DateTimeField(verbose_name=_('Event endtime'))  # 事件故障结束时间
    system_name = models.CharField(max_length=128, verbose_name=_('System name'))  # 事件影响的系统
    event_level = models.SmallIntegerField(  # 事件等级
        choices=EVENT_LEVEL_CHOICES, default='LEVEL_8', max_length=10,
        blank=True, verbose_name=_('Event level')
    )
    event_leader = models.ForeignKey(User, verbose_name=_('Event leader'), on_delete=models.PROTECT)
    # event_ops = models.ManyToManyField(
    #     User, related_name='event',
    #     blank=True, verbose_name=_('Event ops')
    # )
    # event_dev = models.ManyToManyField(
    #     User, related_name='event',
    #     blank=True, verbose_name=_('Event dev')
    # )
    # event_bus = models.ManyToManyField(
    #     User, related_name='event',
    #     blank=True, verbose_name=_('Event bus')
    # )
    # event_ops = models.CharField(
    #     max_length=20, blank=True, null=True, verbose_name=_('Event ops')  # 事件运营负责人
    # )
    # event_dev = models.CharField(
    #     max_length=20, blank=True, null=True, verbose_name=_('Event dev')  # 事件研发负责人
    # )
    # event_bus = models.CharField(
    #     max_length=20, blank=True, null=True, verbose_name=_('Event bus')  # 事件业务负责人
    # )
    comment = models.TextField(
        max_length=1024, blank=True, verbose_name=_('Comment')  # 事件描述
    )
    event_cause = models.TextField(
        max_length=1024, blank=True, verbose_name=_('Event cause')  # 事件根因分析
    )
    event_state = models.SmallIntegerField(
        choices=EVENT_STATE_CHOICES, default='STATE_1', max_length=10,  # 事件状态
        blank=True, verbose_name=_('Event state')
    )
    solve_event_comment = models.TextField(
        max_length=1024, blank=True, verbose_name=_('Solve event comment')  # 事件解决方案
    )
    avoid_event_comment = models.TextField(
        max_length=1024, blank=True, verbose_name=_('Avoid event comment')  # 事件规避方案
    )

    @property
    def get_user(self):
        return self.event_leader.name

    @property
    def get_event_level(self):
        return self.get_event_level_display

    @property
    def get_event_state(self):
        return self.get_event_state_display

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['modified_time']
        verbose_name = _("Event")
