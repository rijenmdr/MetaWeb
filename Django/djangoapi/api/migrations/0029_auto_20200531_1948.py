# Generated by Django 3.0.5 on 2020-05-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_metawebfeedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='photo_1',
        ),
        migrations.RemoveField(
            model_name='website',
            name='photo_2',
        ),
        migrations.RemoveField(
            model_name='website',
            name='photo_3',
        ),
        migrations.RemoveField(
            model_name='website',
            name='photo_4',
        ),
        migrations.RemoveField(
            model_name='website',
            name='photo_5',
        ),
        migrations.AddField(
            model_name='website',
            name='backgroundColor',
            field=models.CharField(default='backgroundColor', max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='featureOneDesH',
            field=models.CharField(default='feature description one', max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='featureThreeDesH',
            field=models.CharField(default='feature description three', max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='featureTwoDesH',
            field=models.CharField(default='feature description two', max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='serviceOne',
            field=models.CharField(default='Service One', max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='serviceOneDes',
            field=models.CharField(default='description of service one', max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='serviceThree',
            field=models.CharField(default='Service Three', max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='serviceThreeDes',
            field=models.CharField(default='description of service three', max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='serviceTwo',
            field=models.CharField(default='Service Two', max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='serviceTwoDes',
            field=models.CharField(default='description of service two', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='addressC',
            field=models.CharField(default='address', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='category',
            field=models.CharField(default='category', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='descriptionC',
            field=models.CharField(default='description', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='descriptionOneH',
            field=models.CharField(default='description one', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='descriptionThreeH',
            field=models.CharField(default='description three', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='descriptionTwoH',
            field=models.CharField(default='description two', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='emailC',
            field=models.CharField(default='email', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='featureOneH',
            field=models.CharField(default='feature One', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='featureThreeH',
            field=models.CharField(default='feature three', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='featureTwoH',
            field=models.CharField(default='feature Two', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='headingOneH',
            field=models.CharField(default='heading One', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='headingThreeH',
            field=models.CharField(default='heading three', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='headingTwoH',
            field=models.CharField(default='Heading Two', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='introductionA',
            field=models.CharField(default='introduction', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='nameOfSiteH',
            field=models.CharField(default='NameOfSite', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='phoneC',
            field=models.CharField(default='phone', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='titleC',
            field=models.CharField(default='title', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='user',
            field=models.CharField(default='user', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='whatWeDoA',
            field=models.CharField(default='what we do', max_length=255),
        ),
    ]
