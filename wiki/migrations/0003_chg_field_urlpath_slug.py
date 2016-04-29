# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_notify', '0001_initial'),
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='URLPath',
            name='slug',
            field=models.SlugField(max_length=255,null=True, verbose_name='slug', blank=True),
        )
    ]
