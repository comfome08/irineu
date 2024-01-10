from django.db import models

class Cantor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)

class Musicas(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    cantor = models.ForeignKey(Cantor, on_delete=models.CASCADE)
    
class Album(models.Model):
    titulo = models.CharField(max_length=100)
    cantor = models.ForeignKey(Cantor, on_delete=models.CASCADE)
    #campo optativo de feats (true or false)
    #ep e classificações
    musicas = models.ManyToManyField(Musicas)
    
class Dados_musicas(models.Model):
    musica = models.ForeignKey(Musicas, on_delete=models.CASCADE)
    streams = models.IntegerField(default=0, verbose_name="Número de Streams de uma música")
    listeners = models.IntegerField(default=0, verbose_name="Número de Ouvintes")
    view = models.IntegerField(default=0, verbose_name="Visualizações dessa música")
    saves = models.IntegerField(default=0, verbose_name="Vezes que essa Música foi salva")
    popularidade = models.IntegerField(default=0, verbose_name="Índice de popularidade")
    data_captura = models.DateTimeField(auto_now_add=True)

class Playlist(models.Model):
    popularidade = models.IntegerField(default=0, verbose_name="Índice de popularidade")
    musica = models.ForeignKey(Musicas, on_delete=models.CASCADE)
    listeners = models.IntegerField(default=0, verbose_name="Número de Ouvintes")
    streams = models.IntegerField(default=0, verbose_name="Número de Streams da PLaylist")
    #algoritimo, spotify, público.

class Audiencia(models.Model):
    ouvintes_total = models.IntegerField(default=0, verbose_name="Ouvintes totais do cantor")
    fluxos_totais = models.IntegerField(default=0, verbose_name=" Número de vezes que sua música foi transmitida por mais de 30 segundos")
    vezes_escutadas = models.IntegerField(default=0, verbose_name=" Número de vezes que sua música foi escutada por cada ouvinte")
    salvamentos_biblioteca = models.IntegerField(default=0, verbose_name=" Número de vezes que sua música foi salva na Biblioteca")
    salvamentos_playlist = models.IntegerField(default=0, verbose_name=" Número de vezes que sua música foi salva na Playlist")
    data_captura = models.DateTimeField(auto_now_add=True)
