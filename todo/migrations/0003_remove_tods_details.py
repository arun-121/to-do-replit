# Generated by Django 3.2.13 on 2022-08-20 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20220820_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tods',
            name='details',
        ),
    ]