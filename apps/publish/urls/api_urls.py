# coding:utf-8
#
from django import urls
from django.urls import path
from rest_framework_bulk.routes import BulkRouter
from .. import api

app_name = 'publish'

rounter = BulkRouter()
rounter.register(r'jenkins', api.JenkinsViewSet, 'jenkins')

urlpatterns = rounter.urls