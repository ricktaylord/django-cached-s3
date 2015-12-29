# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cachedS3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='s3filemeta',
            name='thumbnail',
            field=models.BinaryField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
