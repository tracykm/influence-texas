# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-11 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tpj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='id',
            field=models.IntegerField(db_column='IDNO', db_index=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contributionsummary',
            name='cycle_total',
            field=models.DecimalField(blank=True, db_column='cycle_total', db_index=True, decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='contributionsummary',
            name='donor',
            field=models.ForeignKey(blank=True, db_column='ctrib_ID', on_delete=django.db.models.deletion.CASCADE, related_name='donorsummarys', to='tpj.Donor'),
        ),
        migrations.AlterField(
            model_name='contributionsummary',
            name='filer',
            field=models.ForeignKey(blank=True, db_column='ifiler_ID', on_delete=django.db.models.deletion.CASCADE, related_name='filersummarys', to='tpj.Filer'),
        ),
        migrations.AlterField(
            model_name='contributiontotalbydonor',
            name='cycle_total',
            field=models.DecimalField(blank=True, db_column='cycle_total', db_index=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='contributiontotalbydonor',
            name='donor',
            field=models.OneToOneField(db_column='ctrib_ID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='donortotals', serialize=False, to='tpj.Donor'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='id',
            field=models.IntegerField(db_column='Ctrib_ID', db_index=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='filer',
            name='id',
            field=models.IntegerField(db_column='iFILER_ID', db_index=True, primary_key=True, serialize=False),
        ),
    ]
