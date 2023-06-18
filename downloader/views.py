from django.http import HttpResponse
from django.shortcuts import render
import pytube

def home(request):
    return render(request, 'downloader/index.html')

def download(request):
    if request.method == 'POST':
        video_link = request.POST.get('video_link')
        try:
            yt = pytube.YouTube(video_link)
            stream = yt.streams.get_highest_resolution()
            file_path = stream.download()

            file_name = file_path.split('/')[-1]  # Extract the filename from the file path

            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='video/mp4')
                response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
                return response
        except pytube.exceptions.PytubeError:
            return render(request, 'downloader/error.html')