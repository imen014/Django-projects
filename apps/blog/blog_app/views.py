from django.shortcuts import render , redirect, get_object_or_404
from blog_app.blog import BlogForm
from django.http import HttpResponse
from blog_app.models import Blog


def creation_blog(request):
    """creation blog"""
    blog1 = BlogForm()
    if request.method == "POST":
        blog1 = BlogForm(request.POST)
        if blog1.is_valid():
            blog1.save()
            contenu = "creation avec succées ! "
            return HttpResponse(contenu)
        else:
          redirect('echec.html')
    else:
        blog1 = BlogForm()
        #contenu = "Get Method"
    
    return render(request, 'blog_app/form1.html',{'blog1':blog1})
        
def modifier_article(request, id):
    """modification blog"""
    blog_instance = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        blog_form = BlogForm(request.POST, instance=blog_instance)
        if blog_form.is_valid():
            blog_form.save()
        return HttpResponse("modification reussite")

    else:
        blog_form = BlogForm(instance=blog_instance)
        return render(request, 'blog_app/modifier_blog.html', {'blog_form': blog_form})

    
