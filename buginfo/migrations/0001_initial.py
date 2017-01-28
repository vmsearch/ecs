# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BugInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('info', models.TextField()),
                ('owner', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('public', models.BooleanField(default=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'published time', db_index=True)),
            ],
        ),
    ]
