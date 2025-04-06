# Generated by Django 5.1.7 on 2025-04-05 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PreguntaEncuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PreguntaTrivia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OpcionEncuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opciones', to='interactiva.preguntaencuesta')),
            ],
        ),
        migrations.CreateModel(
            name='OpcionTrivia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('es_correcta', models.BooleanField(default=False)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opciones', to='interactiva.preguntatrivia')),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaEncuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('opcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interactiva.opcionencuesta')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interactiva.preguntaencuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interactiva.pelicula')),
            ],
        ),
    ]
