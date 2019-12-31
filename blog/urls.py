from django.urls import path
from . import views

urlpatterns = [
    path('acceuil', views.home),
    path('article/<int:id_article>', views.view_article, name='afficher_article'),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),

]