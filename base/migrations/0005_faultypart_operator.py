# Generated by Django 4.1 on 2022-09-04 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_operators_planes_operators_planes'),
    ]

    operations = [
        migrations.AddField(
            model_name='faultypart',
            name='operator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.operators'),
        ),
    ]