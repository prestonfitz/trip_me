from django.urls import path
from .views import indexPageView, tripsPageView

app_name = 'travelPages'
urlpatterns = [
    path("", indexPageView, name="index"),
    path("trips/",tripsPageView,name="trips"),
]