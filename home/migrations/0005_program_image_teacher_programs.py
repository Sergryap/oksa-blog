# Generated by Django 4.1 on 2022-08-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_coursestudent_prepayment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='programs_images'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='programs',
            field=models.ManyToManyField(related_name='teachers', through='home.Course', to='home.program'),
        ),
    ]
