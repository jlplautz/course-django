from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('<h3>Olá Django</h3>')
