# Generated by Django 3.2.9 on 2022-01-15 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Common', '0003_phonecode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonecode',
            name='status',
            field=models.PositiveIntegerField(default=1),
        ),
    ]