from django.urls import path
from . import views

urlpatterns = [
    path('', views.req),  #the path for our index view
]