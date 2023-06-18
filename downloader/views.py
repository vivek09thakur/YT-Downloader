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
            stream = yt.streams.filter().get_highest_resolution()
            stream.download()
            render(request, 'downloader/success.html')
        except Exception as e:
            error_message = str(e)
            return render(request, 'downloader/error.html', {'error_message': error_message})

