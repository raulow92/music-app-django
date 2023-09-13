from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),
]