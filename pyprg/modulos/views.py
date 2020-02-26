from django.shortcuts import render

# Create your views here.
from pyprg.modulos import facade


def detalhe(request, slug):
    """
    esta função vai renderizar o template modulos/modulo_detalhe.html
    para apresentar este detalhe precisaremos chegar ao modelo apartir de seu slug passado aqui como paramento
    vamos passar aqui como contexto objecto que vai ter chave 'modulo' e vamos procurar este modulo apartir de seu slug
    Para fazer isto vamos criar mais uma função na facade.encontrar_modulos(slug) e vamos receber o modulo
    :param request:
    :param slug:
    :return:
    """
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.lista_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})


def aula(request, slug):
    aula = facade.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})


def indice(request):
    return render(request, 'modulos/indice.html')
