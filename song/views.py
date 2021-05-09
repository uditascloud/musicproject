from django.shortcuts import render
from song.models import Song

def index(request):
    song=Song.objects.all()
    return render(request, 'song/index.htm', {'song':song})
def songs(request):
    song=Song.objects.all()
    return render (request, 'song/songs.htm', {'song':song})
def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request, 'song/songpost.htm', {'song': song})    
# Create your views here.
