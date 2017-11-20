from django.shortcuts import render, redirect
from .models import Image, tags

def home(request):
    '''
    display all images on home page
    '''
    images = Image.get_images
    return render(request, 'home.html', {"images":images})

def tags(request):
    '''
    display all tags
    '''
    all_tags = tags.get_tags
    print('all_tags')
    return render(request, 'nav_buttons.html', {"all_tags":all_tags})