# Generated by Django 2.2.10 on 2020-03-15 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0024_auto_20200315_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='titulo',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
