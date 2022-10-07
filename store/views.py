from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from store.models import *


def index(request):
    Home = home.objects.all
    shoes=shoe.objects.all()
    # filter(updated)
    
    trends=trending.objects.all


    context = ( 
        {'home' : Home,'Shoe': shoes,'Trending': trends} )
      
    return render(request, 'index.html', context)

def shoes(request):
    shoes=shoe.objects.all
    context = {'Shoe': shoes}
    return render(request, 'shoes.html', context)

def collection(request):
    return render(request, 'collection.html')

def contact(request):
    return render(request, 'contact.html')

def racingshoes(request):
    return render(request, 'racing boots.html')