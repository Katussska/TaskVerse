# Generated by Django 5.0.6 on 2024-05-31 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_firstname_user_lastname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastName',
            new_name='last_name',
        ),
    ]
