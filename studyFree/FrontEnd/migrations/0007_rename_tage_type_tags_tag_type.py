# Generated by Django 3.2.9 on 2022-01-29 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0006_alter_notebook_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='tage_type',
            new_name='tag_type',
        ),
    ]
