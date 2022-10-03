from django.urls import path
from store import views


urlpatterns = [
    path('', views.index, name='index' ),
    path('shoes/', views.shoes, name='shoes'),
    path('collection/', views.collection, name='collection'),
    path('contact/', views.contact, name='contact'),
    path('racingshoes/', views.racingshoes, name='racingshoes'),
]