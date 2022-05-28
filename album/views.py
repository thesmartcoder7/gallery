from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'album/index.html')

    
def all_images(request):
    return render(request, 'album/album.html')