# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0008_add_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='team_members',
            field=models.TextField(blank=True, null=True, verbose_name='team members'),
        ),
    ]
