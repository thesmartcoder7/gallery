from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

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


def check(request):
    if request.method == 'POST':
        category = request.POST['category']
        return redirect('album_category', category = category)


def category(request, category):
    return render(request, 'album/category.html')