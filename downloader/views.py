from django.http import HttpResponse
from django.shortcuts import render
import os
import googleapiclient.discovery
import googleapiclient.errors
import pytube


def home(request):
    return render(request, 'downloader/index.html')


def download(request):

    if request.method == 'POST':
        video_link = request.POST.get('video_link')
        youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey='AIzaSyAvxF1sKntfhUpYM6zm-nvkemfYk9Jf5nY')
        try:
            video_id = pytube.extract.video_id(video_link)
            video_response = youtube.videos().list(part='snippet', id=video_id).execute()
            video_details = video_response['items'][0]['snippet']

            yt = pytube.YouTube(video_link)
            stream = yt.streams.get_highest_resolution()
            file_path = stream.download()
            file_name = os.path.basename(file_path)

            with open(file_path, 'rb') as file:

                response = HttpResponse(file.read(), content_type='video/mp4')
                response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
                response['Content-Disposition'] += '; video_title="{}"'.format(video_details['title'])

                return response
            
        except (pytube.exceptions.PytubeError, googleapiclient.errors.Error):
            return render(request, 'downloader/error.html')
