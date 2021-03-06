# Generated by Django 3.2.6 on 2021-12-20 15:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0012_auto_20211220_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='githubrepos',
            name='content',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='githubrepos',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None), default=[], size=None),
            preserve_default=False,
        ),
    ]
