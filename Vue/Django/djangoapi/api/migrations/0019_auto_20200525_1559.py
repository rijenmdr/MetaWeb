# Generated by Django 3.0.5 on 2020-05-25 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='menu1',
            field=models.CharField(default='menu', max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='menu2',
            field=models.CharField(default='menu', max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='menu3',
            field=models.CharField(default='menu', max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='menus4',
            field=models.CharField(default='menu', max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='menus5',
            field=models.CharField(default='menu', max_length=255),
        ),
    ]