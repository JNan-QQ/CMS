# Generated by Django 3.2.5 on 2021-12-30 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userToken',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('endTime', models.DateField(auto_now=True)),
                ('machineCode1', models.CharField(blank=True, max_length=100, null=True)),
                ('machineCode2', models.CharField(blank=True, max_length=100, null=True)),
                ('machineCode3', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cms_Token',
            },
        ),
    ]
