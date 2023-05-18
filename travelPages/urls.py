from django.urls import path
from .views import indexPageView, tripsPageView, detailsPageView, twitter, facebook, linkedin

app_name = 'travelPages'
urlpatterns = [
    path("", indexPageView, name="index"),
    path("trips/",tripsPageView,name="trips"),
    path("<int:id>/", detailsPageView, name='details'),
    path("twitter/",twitter,name="twitter"),
    path("facebook/",facebook,name="facebook"),
    path("linkedin/",linkedin,name="linkedin")
]