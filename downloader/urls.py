from django.urls import path

from downloader.views import home,download


urlpatterns = [
    path('', home, name='home'),
    path('download/',download,name='download')
]