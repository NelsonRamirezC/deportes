from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView, name='index'),
    path('usuarios/', include('usuarios.urls')),
    path('', include('club.urls')),
    path('api/', include('api.urls')),
]

