# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0006_auto_20170313_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attivita',
            name='giornoEvento',
            field=models.CharField(choices=[('Lunedi', 'Lunedi'), ('Martedi', 'Martedi'), ('Mercoledi', 'Mercoledi'), ('Giovedi', 'Giovedi'), ('Venerdi', 'Venerdi'), ('Sabato', 'Sabato'), ('Domenica', 'Domenica')], max_length=10),
        ),
        migrations.AlterField(
            model_name='attivita',
            name='meseEvento',
            field=models.CharField(choices=[('Gennaio', 'Gennaio'), ('Febbraio', 'Febbraio'), ('Marzo', 'Marzo'), ('Aprile', 'Aprile'), ('Maggio', 'Maggio'), ('Giugno', 'Giugno'), ('Luglio', 'Luglio'), ('Agosto', 'Gennaio'), ('Settembre', 'Settembre'), ('Ottobre', 'Ottobre'), ('Novembre', 'Novembre'), ('Dicembre', 'Dicembre')], max_length=10),
        ),
        migrations.AlterField(
            model_name='attivita',
            name='numEvento',
            field=models.IntegerField(max_length=10),
        ),
    ]
