# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-11 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField(verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
            ],
        ),
    ]