# Generated by Django 4.2.7 on 2024-01-10 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_control', '0002_album_musicas_dados_musicas_data_captura_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ouvintes_total', models.IntegerField(default=0, verbose_name='Ouvintes totais do cantor')),
                ('fluxos_totais', models.IntegerField(default=0, verbose_name=' Número de vezes que sua música foi transmitida por mais de 30 segundos')),
                ('vezes_escutadas', models.IntegerField(default=0, verbose_name=' Número de vezes que sua música foi escutada por cada ouvinte')),
                ('salvamentos_biblioteca', models.IntegerField(default=0, verbose_name=' Número de vezes que sua música foi salva na Biblioteca')),
                ('salvamentos_playlist', models.IntegerField(default=0, verbose_name=' Número de vezes que sua música foi salva na Playlist')),
                ('data_captura', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='listeners',
            field=models.IntegerField(default=0, verbose_name='Número de Ouvintes'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='streams',
            field=models.IntegerField(default=0, verbose_name='Número de Streams da PLaylist'),
        ),
    ]