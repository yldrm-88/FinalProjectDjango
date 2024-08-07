from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('company/', company, name='company'),
    path('about/', about, name='about'),
    path('advert/<int:id>', advert, name='advert'),
    path('match/',match, name='match'),
]
