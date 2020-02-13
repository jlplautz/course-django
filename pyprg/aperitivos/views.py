from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 386792293},
        'instalacao-windows': {'titulo': 'Instalação Wndows', 'vimeo_id': 387145176},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
