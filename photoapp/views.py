from django.shortcuts import render
from django.http import HttpResponse
from .models import  *

# Create your views here.

def images(request):
    images=Image.all_images()
    return render (request, 'images/homepage.html', {"images":images})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        image_results = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'images/search.html',{"message":message,"images": image_results})

    else:
        message = "Please enter a search term"
        return render(request, 'images/search.html',{"message":message})