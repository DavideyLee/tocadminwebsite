from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from orgs.mixins import OrgModelMixin

# Create your models here.

__all__ = ['Event']

class Event(OrgModelMixin):
    LEVEL_1 = 'level_1'
    LEVEL_2 = 'level_2'
    LEVEL_3 = 'level_3'
    LEVEL_4 = 'level_4'
    LEVEL_5 = 'level_5'
    LEVEL_6 = 'level_6'
    LEVEL_7 = 'level_7'
    LEVEL_8 = 'level_7'

    EVENT_LEVEL_CHOICES = (
        (LEVEL_1, _('1 LEVEL')),
        (LEVEL_2, _('2 LEVEL')),
        (LEVEL_3, _('3 LEVEL')),
        (LEVEL_4, _('4 LEVEL')),
        (LEVEL_5, _('5 LEVEL')),
        (LEVEL_6, _('6 LEVEL')),
        (LEVEL_7, _('7 LEVEL')),
        (LEVEL_8, _('8 LEVEL')),
    )

    STATE_1 = 'state_1'
    STATE_2 = 'state_2'
    STATE_3 = 'state_3'
    STATE_4 = 'state_4'
    STATE_5 = 'state_5'


    EVENT_STATE_CHOICES = (
        (STATE_1, _('STATE 1')),
        (STATE_2, _('STATE 2')),
        (STATE_3, _('STATE 3')),
        (STATE_4, _('STATE 4')),
        (STATE_5, _('STATE 5')),

    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=70, verbose_name=_('Title'))   # 事件标题
    created_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_('Create time'))  # 事件记录创建时间
    modified_time = models.DateTimeField(auto_now=True, verbose_name=_('Modified time'))  # 事件记录最后修改时间
    finish_time = models.DateTimeField(verbose_name=_('Finish time'))  # 事件关闭时间
    event_starttime = models.DateTimeField(verbose_name=_('Event starttime'))  # 事件故障开始时间
    event_endtime = models.DateTimeField(verbose_name=_('Event endtime'))  # 事件故障结束时间
    system_name = models.CharField(max_length=128, verbose_name=_('System name'))  # 事件影响的系统
    event_level = models.CharField(  # 事件等级
        choices=EVENT_LEVEL_CHOICES, default='LEVEL_8', max_length=10,
        blank=True, verbose_name=_('Event level')
    )
    event_ops = models.CharField(
        max_length=20, blank=True, null=True, verbose_name=_('Event ops')  # 事件运营负责人
    )
    event_dev = models.CharField(
        max_length=20, blank=True, null=True, verbose_name=_('Event dev')  # 事件研发负责人
    )
    event_bus = models.CharField(
        max_length=20, blank=True, null=True, verbose_name=_('Event bus')  # 事件业务负责人
    )
    comment = models.TextField(
        max_length=1000, blank=True, verbose_name=_('Comment')  # 事件描述
    )
    event_cause = models.TextField(
        max_length=500, blank=True, verbose_name=_('Comment cause')  # 事件根因分析
    )
    event_state = models.CharField(
        choices=EVENT_STATE_CHOICES, default='STATE_1', max_length=10,  # 事件状态
        blank=True, verbose_name=_('Event state')
    )
    solve_event_comment = models.TextField(
        max_length=1000, blank=True, verbose_name=_('Solve event comment')  # 事件解决方案
    )
    avoid_event_comment = models.TextField(
        max_length=1000, blank=True, verbose_name=_('Avoid event comment')  # 事件规避方案
    )