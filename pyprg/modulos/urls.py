from django.urls import path

from pyprg.modulos import views

app_name = 'modulos'
urlpatterns = [
    # <slug> => que no teste demos o nome de motivação
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('aulas/<slug:slug>', views.aula, name='aula'),
    path('', views.indice, name='indice'),
]
