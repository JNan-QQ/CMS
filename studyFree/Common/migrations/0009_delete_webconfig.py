# Generated by Django 3.2.9 on 2022-02-28 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Common', '0008_alter_webconfig_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='webConfig',
        ),
    ]
