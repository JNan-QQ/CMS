# Generated by Django 3.2.9 on 2021-12-31 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userToken', '0002_alter_usertoken_endtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='endTime',
            field=models.DateTimeField(),
        ),
    ]