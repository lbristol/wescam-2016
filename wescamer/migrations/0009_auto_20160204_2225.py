# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wescamer', '0008_student_isregistered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='isRegistered',
            field=models.BooleanField(default=False),
        ),
    ]
