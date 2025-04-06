from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_principal, name='menu_principal'),
    path('trivias/', views.trivias, name='trivias'),
    path('trivias/', views.trivias, name='trivias'),
    path('', views.inicio, name='inicio'),
    path('votacion/', views.votacion, name='votacion'),
    path('encuestas/', views.encuestas, name='encuestas'),
    path('programacion/', views.programacion, name='programacion'),
]
