from django.urls import path, include
from .views import agregar_persona,lista_personas
from . import views

urlpatterns = [
    #path('add_persona/', agregar_persona, name="add_persona"),
    path('add_persona/', views.agregar_persona, name='agregar_persona'),
    path('listado_personas/', views.lista_personas, name='lista_personas'),
]
