# Generated by Django 3.2.9 on 2022-01-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userToken', '0005_order_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField(blank=True, max_length=100, null=True)),
                ('create_time', models.DateField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=100, null=True)),
                ('timeDays', models.IntegerField(blank=True, max_length=100, null=True)),
                ('status', models.IntegerField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'cms_products',
            },
        ),
    ]