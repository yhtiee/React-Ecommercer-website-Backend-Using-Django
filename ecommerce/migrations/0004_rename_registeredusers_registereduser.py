# Generated by Django 4.0.4 on 2022-08-20 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_rename_users_registeredusers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegisteredUsers',
            new_name='RegisteredUser',
        ),
    ]
