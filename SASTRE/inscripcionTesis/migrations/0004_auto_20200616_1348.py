# Generated by Django 2.2.13 on 2020-06-16 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0040_remove_usuario_nombreusuario'),
        ('inscripcionTesis', '0003_tesis_comitetutorial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tesis',
            name='comiteTutorial',
        ),
        migrations.AddField(
            model_name='tesis',
            name='abstrac',
            field=models.CharField(default='', max_length=5000, verbose_name='Abstrac de la tesis'),
        ),
        migrations.AddField(
            model_name='tesis',
            name='director1',
            field=models.CharField(default='', max_length=50, verbose_name='Ingresar nombre de director 1'),
        ),
        migrations.AddField(
            model_name='tesis',
            name='director2',
            field=models.CharField(default='', max_length=50, verbose_name='Ingresar nombre de director 2'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='alumno',
            field=models.CharField(default='', max_length=100, verbose_name='Nombre del alumno autor'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='nombreTesis',
            field=models.CharField(default='', max_length=500, verbose_name='Titulo de la tesis'),
        ),
        migrations.CreateModel(
            name='ComiteTutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miembros', models.ManyToManyField(to='usuario.Profesor')),
                ('tesis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inscripcionTesis.Tesis')),
            ],
        ),
    ]
