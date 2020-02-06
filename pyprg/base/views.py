from django.http import HttpResponse


# Create your views here.

def home(request):
    # raise ValueError() # <= para simular erro para o Sentry
    return HttpResponse('<html><body>Ola Django</body></html>', content_type='text/html')
