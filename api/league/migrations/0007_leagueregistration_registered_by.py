# Generated by Django 2.0 on 2018-03-25 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('league', '0006_remove_leagueregistration_registered_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='leagueregistration',
            name='registered_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
