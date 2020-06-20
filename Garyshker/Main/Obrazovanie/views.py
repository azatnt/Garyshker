from django.shortcuts import render
from .models import *



def show_item(request):
    type = Type.objects.all()
    item = Item.objects.all()
    genre = Genre.objects.all()
    context = {
        'type': type,
        'item': item,
        'genre': genre
    }
    return render(request, 'obrazovanie/obrazovanie.html', context)


def genre_detail(request, slug):
    genre_all = Genre.objects.all()
    genre = Genre.objects.filter(slug=slug)
    return render(request, 'obrazovanie/genre_detail.html', context={'genre':genre, 'genre_all': genre_all})
