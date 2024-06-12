# Generated by Django 5.0.3 on 2024-06-11 09:01

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='sp_id',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='sp_image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='D:\\DESKTOP\\SE_Aquarius Sports Check In\\SE_ASCI\\update'), upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='sp_table',
            name='sp_image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='D:\\DESKTOP\\SE_Aquarius Sports Check In\\SE_ASCI\\update'), upload_to='uploads/'),
        ),
    ]
