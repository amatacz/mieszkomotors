# Generated by Django 4.1.7 on 2023-03-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mieszkomotors', '0002_car_in_mieszkomotors_since_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='attachements',
            field=models.FileField(blank=True, max_length=200, upload_to='documents'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='attachements',
            field=models.FileField(blank=True, max_length=200, upload_to='documents'),
        ),
    ]
