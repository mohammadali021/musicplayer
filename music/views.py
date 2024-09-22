from django.shortcuts import render

from music.models import Song


# Create your views here.
def index(request):
    allsongs = Song.objects.all()
    return render(request , 'music/index.html' , {'allsongs':allsongs})