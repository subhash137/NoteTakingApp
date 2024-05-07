from django.urls import path
from . import views

urlpatterns = [
    path('', views.getroute, name='routes'),
    path('notes/',views.getnotes, name='notes'),
    path('notes/<str:pk>/',views.getnote, name='note')

]