# Generated by Django 3.0.5 on 2020-06-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20200606_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='phone',
            field=models.CharField(default='phone', max_length=255),
        ),
    ]
