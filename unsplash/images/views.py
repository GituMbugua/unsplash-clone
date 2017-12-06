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

def tag_images(request, tag_id):
    try:
        tag = tags.objects.get(id=tag_id)
        images = Image.objects.filter(tags=tag).all()
        print(images)
    except:
        raise Http404()
        
    return render(request, 'tag_images.html', {"tag":tag, "images":images})

def search_results(request):
    if 'tag' in request.GET and request.GET['tag']:
        search_term = request.GET.get('tag')
        searched_tags = tags.search_by_tags(search_term)
        print(searched_tags)
        try:
            tag = searched_tags[0]
            # print(tag)            
            images = Image.objects.filter(tags=tag).all()
            # print(images)                        
        except IndexError:
            raise Http404
        all_tags = tags.get_tags()
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "tags":searched_tags, "images":images, "all_tags":all_tags})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})