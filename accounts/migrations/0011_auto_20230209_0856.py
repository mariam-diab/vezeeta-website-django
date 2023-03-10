# Generated by Django 3.2.17 on 2023-02-09 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default=1, max_length=50, verbose_name='المحافظة'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='address_details',
            field=models.CharField(default=1, max_length=100, verbose_name='العنوان بالتفصيل'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='doctor',
            field=models.CharField(default=1, max_length=50, verbose_name='دكتور؟'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.ImageField(default=1, max_length=12, upload_to='', verbose_name='الهاتف: '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='specialist',
            field=models.CharField(default=1, max_length=50, verbose_name='متخصص في: '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='subtitle',
            field=models.CharField(default=1, max_length=50, verbose_name='نبذة عنك'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='waiting_time',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3, verbose_name='مدة الأنتظار'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='working_hours',
            field=models.CharField(default=1, max_length=50, verbose_name='ساعات العمل: '),
            preserve_default=False,
        ),
    ]
