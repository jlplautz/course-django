# Create your views here.
from django.shortcuts import render


def home(request):
    # return render(request, 'base/home.html', {'MODULOS': facade.listar_modulos_ordenados()})
    return render(request, 'base/home.html', {})
    # raise ValueError() # <= para simular erro para o Sentry
    # return HttpResponse('<html><body>Ola Django</body></html>', content_type='text/html')
