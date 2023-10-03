from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('albums/<int:album_id>/', views.album_detail, name='album_detail'),
    path('artists/import/', views.artist_import, name='artist_import'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)