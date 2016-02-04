# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wescamer', '0003_remove_student_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='crush',
            name='nickname',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
    ]
