# Generated by Django 3.2.5 on 2022-04-21 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pay', '0011_cdk_cdkuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cdkuser',
            old_name='coin',
            new_name='coins',
        ),
        migrations.AlterField(
            model_name='cdk',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
