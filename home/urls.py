from django.urls import path
from . import views

app_name="frontview"

urlpatterns = [
    path('',views.homeView,name='homeView'),
    path('hr',views.hrView,name='hrView'),
    path('legal',views.legalView,name='legalView'),
]