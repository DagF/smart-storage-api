# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 08:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='RFID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('value', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='box.Box')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='box',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='box.Box'),
        ),
    ]
