# Generated by Django 4.1 on 2022-09-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_faultypart_part_alter_faultypart_plane_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='countInStock',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parts',
            name='serialNumber',
            field=models.IntegerField(),
        ),
    ]
