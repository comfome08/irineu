from django.urls import path
from music_control.views import home, assistente

urlpatterns=[
    path('',home),
    path('assistente',assistente)

]