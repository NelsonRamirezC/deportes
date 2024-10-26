from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages

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

class ClubCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Club
    template_name = "club/create_club.html"
    fields = ['nombre', 'liga', 'imagen']
    success_url = reverse_lazy('clubs')
    permission_required = 'club.add_club'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "Usted no tiene el nivel de acceso para acceder a la vista.")
            return redirect("index")
        
        else:
            messages.info(self.request, "Primero debe iniciar sesión para continuar.")
            return redirect("login")
            

# ACTUALIZAR CLUB

class ClubUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Club
    template_name = "club/update_club.html"
    fields = ['nombre', 'liga', 'imagen']
    success_url = reverse_lazy('clubs')
    permission_required = 'club.change_club'
    

# ELIMINAR CLUB
