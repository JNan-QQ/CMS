# Generated by Django 3.2.9 on 2022-01-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userToken', '0006_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='timeDays',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
