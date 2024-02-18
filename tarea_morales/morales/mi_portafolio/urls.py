from django.urls import path
from .views import perfil_peliculas, index, list_profiles, new_profile, view_profile

urlpatterns = [
    path('', index, name='index'),
    path('perfil_peliculas/', perfil_peliculas, name='perfil_peliculas'),
    path('profile/', list_profiles, name='profile'),
    path('profile/new/', new_profile, name='new-profile'),
    path('view/<int:id>/', view_profile, name='view-profile')
]

