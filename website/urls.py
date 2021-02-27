from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('contact', views.contact, name='contact'),
    path('apropos', views.apropos, name='apropos'),
    path('rdv', views.rdv, name='rdv'),
]
