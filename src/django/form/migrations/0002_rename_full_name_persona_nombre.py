# Generated by Django 5.0.7 on 2024-07-14 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='full_name',
            new_name='nombre',
        ),
    ]
