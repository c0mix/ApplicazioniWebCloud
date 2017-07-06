# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0005_auto_20170313_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('year_in_school', models.CharField(max_length=3, choices=[('Gen', 'Gennaio'), ('Feb', 'Febbraio'), ('Mar', 'Marzo'), ('Apr', 'Aprile'), ('Mag', 'Maggio'), ('Giu', 'Giugno'), ('Lug', 'Luglio'), ('Ago', 'Gennaio'), ('Set', 'Settembre'), ('Ott', 'Ottobre'), ('Nov', 'Novembre'), ('Dic', 'Dicembre')])),
            ],
        ),
        migrations.RemoveField(
            model_name='attivita',
            name='dataEvento',
        ),
        migrations.AddField(
            model_name='attivita',
            name='annoEvento',
            field=models.IntegerField(max_length=4, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attivita',
            name='giornoEvento',
            field=models.CharField(max_length=3, choices=[('Lun', 'Lunedi'), ('Mar', 'Martedi'), ('Mer', 'Mercoledi'), ('Gio', 'Giovedi'), ('Ven', 'Venerdi'), ('Sab', 'Sabato'), ('Dom', 'Domenica')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attivita',
            name='meseEvento',
            field=models.CharField(max_length=3, choices=[('Gen', 'Gennaio'), ('Feb', 'Febbraio'), ('Mar', 'Marzo'), ('Apr', 'Aprile'), ('Mag', 'Maggio'), ('Giu', 'Giugno'), ('Lug', 'Luglio'), ('Ago', 'Gennaio'), ('Set', 'Settembre'), ('Ott', 'Ottobre'), ('Nov', 'Novembre'), ('Dic', 'Dicembre')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attivita',
            name='numEvento',
            field=models.IntegerField(max_length=3, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attivita',
            name='oraEvento',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
