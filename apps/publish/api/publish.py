# coding: utf-8
#

from orgs.mixins.api import OrgBulkModelViewSet
from ..hands import IsOrgAdminOrAppUser
from .. import models, serializers


__all__ = ['PublishViewSet']

class PublishViewSet(OrgBulkModelViewSet):
    model = models.JenkinsJobManage
    fillterset_fields = ('name', 'git_repos', 'jenkins_job')
    search_fields = fillterset_fields
    permission_classes = (IsOrgAdminOrAppUser,)
    serializer_class = serializers.PublishSerializer
    
