from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Club, Jugador

class ClubesView(ListView):
    model = Club
    template_name = "club/clubs.html"
    context_object_name = 'clubs'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Página de equipos deportivos'
        return context
    
class ClubDetailView(DetailView):
    model = Club
    template_name = "club/detail_club.html"
    context_object_name = 'club'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jugadores"] = self.object.jugadores.all()
        return context
    
    
# CREAR NUEVOS CLUB

# ACTUALIZAR CLUB

# ELIMINAR CLUB

#> INCLUIR MIXIN DE LOGIN Y PERMISSION