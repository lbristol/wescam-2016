# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.9.1 on 2016-02-01 04:37
from __future__ import unicode_literals

from django.db import migrations
=======
from __future__ import unicode_literals

from django.db import migrations, models
>>>>>>> origin/master


class Migration(migrations.Migration):

    dependencies = [
        ('wescamer', '0002_student_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
    ]
