from django.shortcuts import render, redirect
from django.http import Http404
from .models import Image, tags

def home(request):
    '''
    display all images on home page
    '''
    images = Image.get_images
    all_tags = tags.get_tags()
    return render(request, 'home.html', {"images":images, "all_tags":all_tags})

def image(request, image_id):
    '''
    display an image fullscreen
    '''
    try:
        image = Image.objects.get(id=image_id)
    except:
        raise Http404()
    return render(request, 'image.html', {"image":image})