from django.db import models
from django.utils.translation import ugettext_lazy as _

from orgs.mixins.models import OrgModelMixin
from common.mixins import CommonModelMixin


class JenkinsJobManage(CommonModelMixin, OrgModelMixin):
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    git_repos = models.CharField(max_length=100, verbose_name=_('GitRepos'))
    jenkins_job = models.CharField(max_length=30, verbose_name=_('JenkinsJob'))
    test_ip = models.GenericIPAddressField(null=True,
                                           blank=True,
                                           verbose_name=_('TestIP'))
    pre_ip = models.GenericIPAddressField(verbose_name=_('PreIP'))
    comment = models.TextField(
        max_length=128, default='', blank=True, verbose_name=_('Comment')
    )

    class Meta:
        verbose_name_plural = verbose_name = _("JenkinsJobManage")