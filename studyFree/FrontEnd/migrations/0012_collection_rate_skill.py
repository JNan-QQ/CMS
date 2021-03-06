# Generated by Django 3.2.5 on 2022-05-24 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FrontEnd', '0011_articlecontent_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='默认标题', max_length=100, null=True)),
                ('content', models.TextField(blank=True, default='请在此输入内容，支持markdown语法，不要输入保密信息！', null=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('clicks', models.IntegerField(default=0)),
                ('rate', models.DecimalField(decimal_places=2, default=3.0, max_digits=2)),
                ('status', models.PositiveIntegerField(default=2)),
                ('collection', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rate', models.DecimalField(decimal_places=2, default=3.0, max_digits=2)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_rate_user', to='FrontEnd.skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_collection_user', to='FrontEnd.skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
