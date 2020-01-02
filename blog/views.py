from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import datetime
from blog.models import Article

def home(request) :
    return HttpResponse("""
        <h1>Bienvenue<h1>
    """)

def view_article(request, id_article):
    if id_article > 100:
        return Http404
    return HttpResponse("Vous avez demandé l'article n° {0}".format(id_article))

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2
    return render(request,'blog/addition.html', locals())


def accueil(request):
    """Afficher tous les articles de notre blog"""
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {'derniers_articles' : articles})

def lire(request, id):
    """ Afficher un article complet"""
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/lire.html', {'article' : article})




