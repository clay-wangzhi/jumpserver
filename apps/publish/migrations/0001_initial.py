# Generated by Django 3.1.6 on 2021-06-24 10:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JenkinsJobManage',
            fields=[
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('git_repos', models.CharField(max_length=100, verbose_name='GitRepos')),
                ('jenkins_job', models.CharField(max_length=30, verbose_name='JenkinsJob')),
                ('test_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='TestIP')),
                ('stage_ip', models.GenericIPAddressField(verbose_name='PreIP')),
                ('comment', models.TextField(blank=True, default='', max_length=128, verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'JenkinsJobManage',
                'verbose_name_plural': 'JenkinsJobManage',
            },
        ),
    ]