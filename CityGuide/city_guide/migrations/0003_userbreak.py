# Generated by Django 2.0.2 on 2018-06-01 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('city_guide', '0002_auto_20180601_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBreak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('time', models.IntegerField(default=1)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_guide.Tour')),
            ],
        ),
    ]
