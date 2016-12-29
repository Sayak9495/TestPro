# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_album_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='is_favorite',
        ),
    ]
