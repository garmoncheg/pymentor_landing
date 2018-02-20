# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-19 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180219_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='homepage',
            name='team_description',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.TeamDescription'),
        ),
    ]
