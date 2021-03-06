# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-11 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название услуги')),
                ('content', models.TextField(verbose_name='Содержание')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceTypeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='Название категории услуг')),
                ('order', models.PositiveSmallIntegerField(db_index=True, default=0, verbose_name='Порядковый номер')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержание')),
            ],
            options={
                'verbose_name': 'Категория услуг',
                'verbose_name_plural': 'Категории услуг',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='service_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.ServiceTypeModel', verbose_name='Категория услуги'),
        ),
    ]
