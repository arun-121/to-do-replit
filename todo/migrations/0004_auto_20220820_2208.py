# Generated by Django 3.2.13 on 2022-08-20 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_tods_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField()),
                ('completed_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Task',
            },
        ),
        migrations.DeleteModel(
            name='Tods',
        ),
    ]
