from django.urls import path
from . import views

urlpatterns = [
    path('v1/jugadores/', views.jugadores, name='api_jugadores'),
    path('v1/jugadores/delete/<int:pk>', views.delete_jugadores, name='api_delete_jugadores'), 
    path('v1/jugadores/add', views.crear_jugador, name='api_add_jugador'), 
#     path('v1/clubs/', views.clubs, name='api_clubes'),
]