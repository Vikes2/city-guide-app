# Generated by Django 2.0.4 on 2018-04-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city_guide', '0008_auto_20180420_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_path',
            field=models.CharField(max_length=255),
        ),
    ]