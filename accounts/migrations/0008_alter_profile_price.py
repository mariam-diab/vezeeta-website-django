# Generated by Django 3.2.17 on 2023-02-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='سعر الكشف: '),
        ),
    ]