from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from music_control.models import Cantor, Musicas, Album, Dados_musicas
import plotly.express as px

def home(request):
    return render(request,'home.html')

def assistente(request):
    return HttpResponse(request)

def graficos_spotify(request):
    graficos_cantor = Cantor.objects.all()
    graficos_musicas = Musicas.objects.all()
    graficos_album = Album.objects.all()
    graficos_dados_musicas = Dados_musicas.objects.all()

    fig = px.line(
        y=[c.date for c in graficos_cantor],
        x=[c.average for c in graficos_musicas]   
    )

    chart = fig.to_html()
    context = {'chart':chart}
    return render(request,'core/chart.html', context)