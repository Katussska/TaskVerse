# Generated by Django 5.0.6 on 2024-05-11 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TaskPriority',
            new_name='Priority',
        ),
        migrations.RenameModel(
            old_name='TaskTag',
            new_name='Tag',
        ),
    ]
