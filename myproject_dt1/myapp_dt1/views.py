from django.shortcuts import render
from django.http import HttpResponse
from myapp_dt1.models import Bd1

def afficherpage1(request):
    decouvert = Bd1(username="sahar",job="teacher")
    decouvert.save()
    if decouvert.pk is not None:
        contenu = f'{decouvert.username} welcome to {decouvert.job}'
        return HttpResponse(contenu)
    else:
        return HttpResponse("l'enregistrement à echoué ")