# Generated by Django 3.2.17 on 2023-02-10 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_profile_join_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='join_us',
        ),
    ]