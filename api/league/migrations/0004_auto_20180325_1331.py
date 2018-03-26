# Generated by Django 2.0 on 2018-03-25 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0003_league_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='seasons',
        ),
        migrations.AddField(
            model_name='season',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='league.League'),
        ),
    ]
