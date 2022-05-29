from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'album/index.html')

    
def all(request):
    print(Image.objects.all()[0].image)
    context = {
        'all_images': Image.objects.all(),
        'all_locations': Location.objects.all(),
        'all_categories': Category.objects.all()
    }

    return render(request, 'album/album.html', context=context)