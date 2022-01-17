# Generated by Django 3.2.9 on 2022-01-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Common', '0004_alter_phonecode_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCode',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='123456', max_length=100, null=True)),
                ('status', models.PositiveIntegerField(default=1)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'study_email_code',
            },
        ),
        migrations.DeleteModel(
            name='PhoneCode',
        ),
    ]