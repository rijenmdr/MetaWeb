# Generated by Django 3.0.5 on 2020-05-25 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200525_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='website',
            old_name='menus4',
            new_name='menu4',
        ),
        migrations.RenameField(
            model_name='website',
            old_name='menus5',
            new_name='menu5',
        ),
    ]
