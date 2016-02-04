# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wescamer', '0004_crush_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='firstName',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='lastName',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.IntegerField(default=2016),
            preserve_default=False,
        ),
    ]
