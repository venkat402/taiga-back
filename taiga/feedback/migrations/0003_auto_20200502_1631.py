# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-02 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_feedbackentry_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackentry',
            name='subject',
            field=models.CharField(default='', max_length=255, verbose_name='subject'),
        ),
    ]
