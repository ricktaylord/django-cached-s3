# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cachedS3', '0003_auto_20150705_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filetag',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
