# Generated by Django 4.1.2 on 2022-10-15 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_album_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
