from django.urls import path
from . import views

app_name="frontview"

urlpatterns = [
    path('',views.homeView,name='homeView'),
    path('hr',views.hrView,name='hrView'),
    path('legal',views.legalView,name='legalView'),
    path('jobs/<str:section>',views.sectionView,name="sectionView"),
    path('<int:article_id>/<slug:article_slug>',views.articleView,name="articleView"),
]