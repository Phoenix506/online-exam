# Generated by Django 3.1.7 on 2022-05-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_newuser_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='point',
            field=models.IntegerField(default='0', verbose_name='İlkin bal'),
        ),
    ]
