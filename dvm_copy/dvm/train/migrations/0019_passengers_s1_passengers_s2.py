# Generated by Django 5.0 on 2024-01-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0018_journeys'),
    ]

    operations = [
        migrations.AddField(
            model_name='passengers',
            name='s1',
            field=models.CharField(default=True, max_length=34),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passengers',
            name='s2',
            field=models.CharField(default=True, max_length=34),
            preserve_default=False,
        ),
    ]
