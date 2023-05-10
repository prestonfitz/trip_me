from django.shortcuts import render
from .models import tripInfo

# Create your views here.
def indexPageView(request):
    ti = tripInfo.objects.all()

    context = {
        "ti" : ti
    }
    return render(request, 'travelPages/index.html',context)

def tripsPageView(request) :
    ti = tripInfo.objects.all()

    context = {
        "ti" : ti
    }
    return render(request, 'travelPages/trips.html',context)

def detailsPageView(request, id):

   ti=tripInfo.objects.get(id=id)

   context = {
      "ti" : ti
   }

   return render(request,'travelPages/details.html', context)