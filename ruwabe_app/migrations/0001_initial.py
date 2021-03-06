# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-08 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guarantors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=15)),
                ('relationship', models.CharField(max_length=50)),
                ('workmate', models.CharField(max_length=150)),
                ('occupation', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=150, null=True)),
                ('phone_number', models.CharField(max_length=150, null=True)),
                ('source', models.URLField(max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ruwabe_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='WorkInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation_details', models.CharField(max_length=150, null=True)),
                ('earnings_range_per_month', models.FloatField(max_length=150, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ruwabe_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='guarantors',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ruwabe_app.User'),
        ),
    ]
