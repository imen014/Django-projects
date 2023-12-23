from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article_Blog_bd

def afficher_liste_article(request):
    articles = Article_Blog_bd.objects.all()
    return render(request,
                  'blog/liste_articles.html',
                  {"articles":articles})


def detail_article(request, id):
    article = Article_Blog_bd.objects.get(id=id)
    return render(request,
                  'blog/article_detail.html',
                  {"article":article})

"""5. **Créer une page de détail :**
   - Exercice : Ajoutez une vue de détail qui permet aux utilisateurs de voir un article de blog
 en détail lorsqu'ils cliquent sur son titre. Créez une nouvelle URL pour cette vue.
"""

    