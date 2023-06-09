# Generated by Django 4.1.3 on 2023-06-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0009_alter_todo_created_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='todo',
            name='tag',
        ),
        migrations.AddField(
            model_name='todo',
            name='tags',
            field=models.ManyToManyField(blank=True, to='todoapp.tag'),
        ),
    ]
