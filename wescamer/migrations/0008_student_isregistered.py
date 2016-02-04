# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wescamer', '0007_auto_20160204_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='isRegistered',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
