# Generated by Django 4.0.4 on 2022-08-21 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_alter_registereduser_registerd_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registereduser',
            old_name='registerd_user',
            new_name='register_user',
        ),
    ]