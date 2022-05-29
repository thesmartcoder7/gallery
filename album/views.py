from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    return render(request, 'album/index.html')

    
def all(request):
    context = {
        'all_images': Image.objects.all(),
        'all_locations': Location.objects.all(),
        'all_categories': Category.objects.all()
    }
    return render(request, 'album/album.html', context=context)


def check(request):
    if request.method == 'POST':
        if request.POST['category'] == 'all':
            return redirect('album_all')
        else:
            return redirect('album_category', category = request.POST['category'] )
    else:
        return redirect('album_all')


def category(request, category):
    context = {
            'all_images': Image.objects.all(),
            'all_locations': Location.objects.all(),
            'all_categories': Category.objects.all(),
            'category': category
        }
    return render(request, 'album/category.html', context = context)



def handle_not_found(request, exception):
    return render(request, 'album/not-found.html')