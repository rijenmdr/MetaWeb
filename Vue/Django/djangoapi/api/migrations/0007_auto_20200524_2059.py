# Generated by Django 3.0.5 on 2020-05-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
