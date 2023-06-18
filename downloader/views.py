from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
import pytube
import shutil
import os

def home(request):
    return render(request, 'downloader/index.html')

def download(request):
    if request.method == 'POST':
        video_link = request.POST.get('video_link')
        try:
            yt = pytube.YouTube(video_link)
            stream = yt.streams.filter(progressive=True,
                                       resolution='720p',
                                       fps=60,res='max',
                                       file_extension='mp4'
                                    ).first()
            # stream.download()
            file_path = stream.download()
            # render(request, 'downloader/success.html')
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='video/mp4')
                response['Content-Disposition'] = 'attachment; filename="{0}"'.format(stream.default_filename)
                return response
        except Exception as e:
            error_message = str(e)
            return render(request, 'downloader/error.html', {'error_message': error_message})

