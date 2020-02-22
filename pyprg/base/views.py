# Create your views here.
from django.shortcuts import render

from pyprg.modulos import facade


def home(request):
    return render(request, 'base/home.html', {'MODULOS': facade.listar_modulos_ordenados()})
    # raise ValueError() # <= para simular erro para o Sentry
    # return HttpResponse('<html><body>Ola Django</body></html>', content_type='text/html')
