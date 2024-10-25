from django.contrib import admin
from .models import Club, Jugador


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'liga']
    list_display = ['nombre', 'liga']
    ordering = ['nombre']
    
    
@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'posicion']
    list_display = ['nombre', 'apellido', 'posicion', 'club']
    ordering = ['apellido']