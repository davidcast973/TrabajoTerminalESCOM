# Generated by Django 2.2.10 on 2020-03-24 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuario', '0036_remove_profesor_tiramaterias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nombreUsuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]