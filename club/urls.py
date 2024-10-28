from django.urls import path
from . import views

urlpatterns = [
    path('clubs/', views.ClubesView.as_view(), name='clubs'),
    path('clubs/detail/<int:pk>', views.ClubDetailView.as_view(), name='club_detail'),
    path('clubs/create', views.ClubCreateView.as_view(), name='create_club'),
    path('clubs/update/<int:pk>', views.ClubUpdateView.as_view(), name='update_club'),
    path('clubs/delete/<int:pk>', views.ClubDeleteView.as_view(), name='delete_club'),
    path('jugadores/detail/<int:pk>', views.JugadorDetailView.as_view(), name='jugador_detail'),
]