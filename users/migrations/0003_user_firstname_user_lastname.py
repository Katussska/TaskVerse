# Generated by Django 5.0.6 on 2024-05-13 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_name_user_last_login_user_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='firstName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='lastName',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
