# Generated by Django 4.1.3 on 2023-06-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_alter_todo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='tag',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
