# Generated by Django 3.2.17 on 2023-02-10 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_profile_join_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='join_us',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name=': y'),
        ),
    ]