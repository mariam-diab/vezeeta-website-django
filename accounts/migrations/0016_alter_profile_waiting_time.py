# Generated by Django 3.2.17 on 2023-02-10 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_rename_join_us_profile_join_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='waiting_time',
            field=models.DecimalField(decimal_places=0, max_digits=2, verbose_name='مدة الأنتظار بالدقيقة'),
        ),
    ]
