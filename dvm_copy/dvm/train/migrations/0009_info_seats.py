# Generated by Django 5.0 on 2023-12-25 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0008_info_alter_train_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='seats',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]