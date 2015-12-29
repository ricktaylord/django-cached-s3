# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cachedS3', '0002_s3filemeta_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filetag',
            name='name',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
