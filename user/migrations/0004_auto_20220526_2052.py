# Generated by Django 3.1.7 on 2022-05-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220526_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='group',
            field=models.CharField(max_length=100, verbose_name='Qrupunuz'),
        ),
    ]
