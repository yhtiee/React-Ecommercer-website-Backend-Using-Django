# Generated by Django 4.0.4 on 2022-08-21 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_remove_registereduser_register_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='RegisteredUser',
        ),
    ]