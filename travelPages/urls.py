from django.urls import path
from .views import indexPageView, tripsPageView, detailsPageView

app_name = 'travelPages'
urlpatterns = [
    path("", indexPageView, name="index"),
    path("trips/",tripsPageView,name="trips"),
    path("<int:id>/", detailsPageView, name='details'),
]