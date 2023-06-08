from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
import pytube

def home(request):
    return render(request, 'index.html')

def download(request):
    if request.method == 'POST':
        video_link = request.POST.get('video_link')
        try:
            yt = pytube.YouTube(video_link)
            stream = yt.streams.first()
            stream.download()
            return render(request, 'success.html')
        except Exception as e:
            error_message = str(e)
            return render(request, 'error.html', {'error_message': error_message})

