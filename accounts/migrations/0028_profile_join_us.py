# Generated by Django 3.2.17 on 2023-02-10 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_remove_profile_join_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='join_us',
            field=models.CharField(default='2023-02-10', max_length=20),
        ),
    ]
