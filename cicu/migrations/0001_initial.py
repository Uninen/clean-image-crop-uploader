# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-29 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('file', models.FileField(upload_to=b'ajax_uploads/', verbose_name='file')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'uploaded file',
                'verbose_name_plural': 'uploaded files',
            },
        ),
    ]
