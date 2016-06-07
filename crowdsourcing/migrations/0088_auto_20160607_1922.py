# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0087_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='returnfeedback',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='returnfeedback',
            old_name='created_timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='returnfeedback',
            old_name='last_updated',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='returnfeedback',
            name='deleted',
        ),
        migrations.AddField(
            model_name='returnfeedback',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
