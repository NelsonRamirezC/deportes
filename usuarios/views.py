from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages


# VISTA BASADA EN CLASE PARA REGISTRO
class UserRegistroView(CreateView):
    form_class =  UserCreationForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, 'Registro realizo con éxito.')
        return super().form_valid(form)
    
    

# VISTA BASADA EN CLASE PARA LOGIN
class UserLoginView(LoginView):
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    
    def form_valid(self, form):
        messages.success(self.request, 'Login exitoso.')
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return self.get_redirect_url() or self.success_url
    
    
#vista de logout