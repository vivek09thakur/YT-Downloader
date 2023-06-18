from django.urls import path

from .views import home,download


urlpatterns = [
    path('', home, name='home'),
    path('download/',download,name='download')
]