# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='avatar',
            field=models.ImageField(null=True, upload_to=b'avatars/'),
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
