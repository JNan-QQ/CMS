# Generated by Django 3.2.9 on 2022-02-28 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pay', '0009_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='payconfig',
            name='web_url',
            field=models.TextField(default={}),
        ),
    ]
