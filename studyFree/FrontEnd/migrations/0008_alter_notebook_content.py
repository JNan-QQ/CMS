# Generated by Django 3.2.5 on 2022-03-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0007_rename_tage_type_tags_tag_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='content',
            field=models.TextField(blank=True, default='请在此输入内容，支持markdown语法，不要输入保密信息！', null=True),
        ),
    ]
