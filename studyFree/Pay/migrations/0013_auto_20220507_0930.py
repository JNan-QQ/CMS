# Generated by Django 3.2.5 on 2022-05-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pay', '0012_auto_20220421_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='F',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='Z',
            field=models.FloatField(default=0),
        ),
    ]
