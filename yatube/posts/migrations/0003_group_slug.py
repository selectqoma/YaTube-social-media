# Generated by Django 2.2.9 on 2021-06-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210620_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default='group', unique=True),
        ),
    ]
