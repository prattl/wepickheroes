# Generated by Django 2.0 on 2018-03-25 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0005_auto_20180325_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leagueregistration',
            name='registered_by',
        ),
    ]
