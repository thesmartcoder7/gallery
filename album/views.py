from django.shortcuts import render, redirect
from .models import *


def home(request):
    """
    Renders the home page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered home page.

    """
    return render(request, 'album/index.html')


def all(request):
    """
    Renders the album page with all images, locations, and categories.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered album page.

    """
    context = {
        'all_images': Image.objects.all(),
        'all_locations': Location.objects.all(),
        'all_categories': Category.objects.all()
    }
    return render(request, 'album/album.html', context=context)


def check(request):
    """
    Handles the check form submission.

    If the form is submitted with the category 'all', redirects to the 'album_all' URL.
    Otherwise, redirects to the 'album_category' URL with the selected category.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response for the redirect.

    """
    if request.method == 'POST':
        if request.POST['category'] == 'all':
            return redirect('album_all')
        else:
            return redirect('album_category', category=request.POST['category'])
    else:
        return redirect('album_all')


def category(request, category):
    """
    Renders the category page with images, locations, categories, and the selected category.

    Parameters:
        request (HttpRequest): The HTTP request object.
        category (str): The selected category.

    Returns:
        HttpResponse: The HTTP response containing the rendered category page.

    """
    context = {
        'all_images': Image.objects.all(),
        'all_locations': Location.objects.all(),
        'all_categories': Category.objects.all(),
        'category': category
    }
    return render(request, 'album/category.html', context=context)


def handle_not_found(request, exception):
    """
    Handles the 404 not found error.

    Parameters:
        request (HttpRequest): The HTTP request object.
        exception: The exception object representing the error.

    Returns:
        HttpResponse: The HTTP response containing the rendered not-found page.

    """
    return render(request, 'album/not-found.html')
