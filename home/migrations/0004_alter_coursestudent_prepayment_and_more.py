# Generated by Django 4.1 on 2022-08-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_teacher_phone_teacher_social_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursestudent',
            name='Prepayment',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Предоплата'),
        ),
        migrations.AlterField(
            model_name='program',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Телефон'),
        ),
    ]
