from django.shortcuts import render

from pyprg.aperitivos.models import Video

videos = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id=386792293),
    Video(slug='instalacao-windows', titulo='Instalação Windows', vimeo_id=387145176),
]


videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
