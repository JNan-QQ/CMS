# Generated by Django 3.2.5 on 2022-05-10 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pay', '0013_auto_20220507_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='payconfig',
            name='article',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='payconfig',
            name='click',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='payconfig',
            name='notebook',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
