# Generated by Django 4.1.3 on 2023-06-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_on',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]