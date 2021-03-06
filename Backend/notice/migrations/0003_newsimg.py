# Generated by Django 3.2.9 on 2021-11-29 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_message_messagereceiver'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsImg',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.news')),
            ],
        ),
    ]
