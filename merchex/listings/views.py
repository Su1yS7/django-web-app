from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands0 = Band.objects.all()
    return render(request, 'listings/hello.html',{'bands': bands0})


def about(request):
    return render(request, 'listings/about.html')


def listings(request) :
    titres=Listing.objects.all()
    return render(request, 'listings/listings.html', {'titres': titres})
   

def contact(request):
    return render(request, 'listings/contact.html')


