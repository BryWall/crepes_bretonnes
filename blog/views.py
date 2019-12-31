from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import datetime

def home(request) :
    return HttpResponse("""
        <h1>Bienvenue<h1>
    """)

def view_article(request, id_article):
    if id_article > 100:
        return Http404
    return HttpResponse("Vous avez demaandé l'article n° {0}".format(id_article))

def date_actuelle(request):
    return render(request, 'blog/date.html', { 'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2
    return render(request,'blog/addition.html', locals())




