# Generated by Django 3.2.13 on 2022-08-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=500)),
                ('do_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Tods',
            },
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
