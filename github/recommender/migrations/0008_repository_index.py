# Generated by Django 3.2.6 on 2021-12-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0007_auto_20211219_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='index',
            field=models.IntegerField(default=0),
        ),
    ]