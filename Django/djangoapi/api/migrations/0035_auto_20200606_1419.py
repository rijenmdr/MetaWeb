# Generated by Django 3.0.5 on 2020-06-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='backgroundColor',
            field=models.CharField(default='youtubeLink', max_length=255),
        ),
        migrations.AddField(
            model_name='hotel',
            name='category',
            field=models.CharField(default='category', max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='about',
            field=models.CharField(default='about', max_length=555),
        ),
    ]
