# Generated by Django 5.0 on 2023-12-31 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0014_rename_fare_train_fare1_train_fare2_train_fare3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='fare1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='fare2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='fare3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='fareg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='fares',
            field=models.IntegerField(default=0),
        ),
    ]