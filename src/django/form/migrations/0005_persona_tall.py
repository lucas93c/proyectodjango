# Generated by Django 5.0.7 on 2024-07-18 23:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_talleres'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='tall',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='form.talleres'),
        ),
    ]
