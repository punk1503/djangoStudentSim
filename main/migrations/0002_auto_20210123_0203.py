# Generated by Django 3.1.5 on 2021-01-22 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentstats',
            name='date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='studentstats',
            name='ha',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentstats',
            name='hp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentstats',
            name='iq',
            field=models.IntegerField(default=0),
        ),
    ]
