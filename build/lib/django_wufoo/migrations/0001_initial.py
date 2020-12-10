# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-16 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WufooEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_id', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Wufoo entries',
            },
        ),
        migrations.CreateModel(
            name='WufooField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wufoo_id', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('field_type', models.CharField(blank=True, max_length=255, null=True)),
                ('choices', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WufooFieldEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_wufoo.WufooField')),
            ],
            options={
                'verbose_name_plural': 'Wufoo field entries',
                'ordering': ['field', 'subfield'],
            },
        ),
        migrations.CreateModel(
            name='WufooForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WufooSubField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wufoo_id', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('default_val', models.TextField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_wufoo.WufooField')),
            ],
            options={
                'verbose_name': 'Wufoo subfield',
                'verbose_name_plural': 'Wufoo subfields',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='wufoofieldentry',
            name='subfield',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_wufoo.WufooSubField'),
        ),
        migrations.AddField(
            model_name='wufoofieldentry',
            name='wufoo_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_wufoo.WufooEntry'),
        ),
        migrations.AddField(
            model_name='wufoofield',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_wufoo.WufooForm'),
        ),
        migrations.AddField(
            model_name='wufooentry',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_wufoo.WufooForm'),
        ),
    ]