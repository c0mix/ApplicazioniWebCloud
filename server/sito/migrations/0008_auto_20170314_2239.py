# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0007_auto_20170313_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attivita',
            name='annoEvento',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='attivita',
            name='meseEvento',
            field=models.CharField(max_length=10, choices=[('Gennaio', 'Gennaio'), ('Febbraio', 'Febbraio'), ('Marzo', 'Marzo'), ('Aprile', 'Aprile'), ('Maggio', 'Maggio'), ('Giugno', 'Giugno'), ('Luglio', 'Luglio'), ('Agosto', 'Agosto'), ('Settembre', 'Settembre'), ('Ottobre', 'Ottobre'), ('Novembre', 'Novembre'), ('Dicembre', 'Dicembre')]),
        ),
        migrations.AlterField(
            model_name='attivita',
            name='numEvento',
            field=models.IntegerField(),
        ),
    ]
