from django.shortcuts import redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from club.models import Club, Jugador


@require_http_methods(["GET"])
def jugadores(request):
        jugadores = Jugador.objects.select_related('club')
        
        data_jugadores = []
        
        for jugador in jugadores:
            data_jugadores.append({
                "id": jugador.id,
                "nombre": jugador.nombre,
                "club": jugador.club.nombre
            })
        return JsonResponse(data_jugadores, safe=False)
    
@require_http_methods(["DELETE"])
@csrf_exempt
def delete_jugadores(request, pk):
        jugador = get_object_or_404(Jugador, pk=pk)
        
        jugador.delete()
        respuesta = {
            "message": "Jugador eliminado correctamente."
        }
        return JsonResponse(respuesta, safe=False)
    
    

@require_http_methods(["POST"])
@csrf_exempt
def crear_jugador(request):
    
        data_dict = json.loads(request.body) #obtenemos los datos enviados en json desde el cliente
        
        print(data_dict)
        
        club = Club.objects.get(id=data_dict["club"])
        
        nuevo_jugador = Jugador.objects.create(
            nombre=data_dict["nombre"],
            apellido=data_dict["apellido"],
            dorsal=data_dict["dorsal"],
            posicion=data_dict["posicion"],
            club=club
        )

        respuesta = {
            "message": f"Jugador creado con ID: {nuevo_jugador.id}" 
        }
        return JsonResponse(respuesta, safe=False)
