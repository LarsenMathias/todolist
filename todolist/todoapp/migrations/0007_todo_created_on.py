# Generated by Django 4.1.3 on 2023-06-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_todo_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_on',
            field=models.TimeField(blank=True, null=True),
        ),
    ]