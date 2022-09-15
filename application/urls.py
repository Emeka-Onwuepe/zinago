from django.urls import path
from . import views

app_name="applications"

urlpatterns = [
    path('<int:article_id>',views.applicationView,name='applications'),
    path('<int:app_id>/<str:action>',views.process_application,name='process'),
]