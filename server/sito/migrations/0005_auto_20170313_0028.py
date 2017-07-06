# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0004_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attivita',
            old_name='data',
            new_name='dataEvento',
        ),
    ]
