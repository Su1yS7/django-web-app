from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html')


def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch !</p>')

def listings(request) :
    titres=Listing.objects.all()
    return HttpResponse(f"""
        <h1>Les titres de mes groupes préférés sont :</h1>
        <ul>
            <li>{titres[0].title}</li>
            <li>{titres[1].title}</li>
            <li>{titres[2].title}</li>
        </ul>
    """)
   

def contact(request):
    return HttpResponse('<h1>Bienvenu dans contact-us</h1>')


