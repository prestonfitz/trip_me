from django.shortcuts import render

# Create your views here.
def indexPageView(request):
    return render(request, 'travelPages/index.html')