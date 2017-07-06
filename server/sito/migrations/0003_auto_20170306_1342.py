# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0002_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last locals')),
                ('nome', models.CharField(max_length=20)),
                ('cognome', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='attivita',
            name='data',
            field=models.DateTimeField(help_text='formato YYYY-MM-DDThh:mm:ss', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='attivita',
            name='organizzatore',
            field=models.ForeignKey(default='0', to='sito.Sportivo'),
        ),
        migrations.AlterField(
            model_name='attivita',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='attivita', default='0'),
        ),
        migrations.AlterField(
            model_name='sportivo',
            name='data_nascita',
            field=models.DateField(default='01/01/1900', blank=True),
        ),
        migrations.AlterField(
            model_name='sportivo',
            name='luogo_nascita',
            field=models.CharField(default='', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='sportivo',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sportivi', default='0'),
        ),
        migrations.AlterField(
            model_name='sportivo',
            name='paese_nascita',
            field=models.CharField(default='', blank=True, max_length=100),
        ),
    ]
