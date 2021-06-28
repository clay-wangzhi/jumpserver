# coding:utf-8
#
from django.utils.translation import ugettext_lazy as _
from django.db.models import Prefetch, fields
from rest_framework import serializers

from common.drf.serializers import AdaptedBulkListSerializer
from orgs.mixins.serializers import BulkOrgResourceModelSerializer
from django.db.models import Count
from ..models import JenkinsJobManage

__all__ = [
    'JenkinsSerializer',
]



class JenkinsSerializer(BulkOrgResourceModelSerializer):
    class Meta:
        model = JenkinsJobManage
        list_serializer_class = AdaptedBulkListSerializer
        fields_mini = ['id', 'name', 'git_repos', 'jenkins_job', 'pre_ip']
        fields_small = fields_mini + [
            'comment', 'date_created', 'created_by'
        ]
        fields = fields_mini + fields_small + [
            'test_ip',
        ]
        # extra_kwargs = {
        #     'git_repos': {'label': _('GitRepos')},
        #     'jenkins_job': {'label': _('JenkinsJob')},
        #     'pre_ip': {'label': _('PreIP')},
        #     'test_ip': {'label': _('TestIP')},
        # }