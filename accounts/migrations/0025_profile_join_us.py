# Generated by Django 3.2.17 on 2023-02-10 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='join_us',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]