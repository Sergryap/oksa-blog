# Generated by Django 4.1 on 2022-08-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_programdetail_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programdetail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='program_blok_images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='programgallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='program_gallery_images', verbose_name='Изображение'),
        ),
    ]
