# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-05 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_openpay', '0002_auto_20160805_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='trial_end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Trial days'),
        ),
    ]
