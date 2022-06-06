# Generated by Django 3.2.5 on 2022-05-10 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FrontEnd', '0010_alter_articlecontent_clicks'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecontent',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Common.user'),
            preserve_default=False,
        ),
    ]