from django.urls import path

from pyprg.aperitivos.views import video

app_name = 'aperitivos'
urlpatterns = [
    # <slug> => que no teste demos o nome de motivação
    path('<slug:slug>', video, name='video'),
]
