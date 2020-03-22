from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from pastors.models import pastor
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings': listings,
        
    }
    return render(request,'pages/index.html',context)

def about(request):
    #Get all realtors
    realtors=pastor.objects.order_by('church')

    #Get MVP
    mvp_realtors=pastor.objects.all().filter(is_mvp=True)

    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }
    return render(request,'pages/about.html',context)
