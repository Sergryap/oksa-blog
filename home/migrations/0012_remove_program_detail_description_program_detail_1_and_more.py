# Generated by Django 4.1 on 2022-08-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_program_detail_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='detail_description',
        ),
        migrations.AddField(
            model_name='program',
            name='detail_1',
            field=models.TextField(blank=True, null=True, verbose_name='Детальное описание 1'),
        ),
        migrations.AddField(
            model_name='program',
            name='detail_2',
            field=models.TextField(blank=True, null=True, verbose_name='Детальное описание 2'),
        ),
    ]
