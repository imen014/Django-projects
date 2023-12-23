"""
URL configuration for books_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books_management_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('afficher_form/', views.afficher_form),
    path('validation_formulaire/', views.validation_formulaire),
    path('save_books_in_bd/', views.save_books_in_bd),
    path('afficher_liste_livres/', views.afficher_liste_livres),
    path('update_data/<int:id>/update', views.update_data),
    path('supprimer_livres/<int:id>/', views.supprimer_livres),
]
