# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='S3FileMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(unique=True, max_length=255)),
                ('last_modified', models.DateTimeField(null=True, blank=True)),
                ('size', models.IntegerField(null=True, blank=True)),
                ('image_x', models.IntegerField(null=True, blank=True)),
                ('image_y', models.IntegerField(null=True, blank=True)),
                ('tags', models.ManyToManyField(to='cachedS3.FileTag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
