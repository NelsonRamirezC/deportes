from django.db import models

class Club(models.Model):
    DIVISIONES = [
        ('Primera A', 'Primera división'),
        ('Primera B', 'Segunda división'),
        ('Sin división', 'club sin división'),
    ]
    
    nombre = models.CharField(max_length=100, blank=False, null=False)
    liga = models.CharField(max_length=100, blank=False, null=False, choices=DIVISIONES, default='Sin división')
    imagen = models.URLField(null=True)
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        permissions = [("can_edit_clubes", "Puede editar clubes")]
    
    

class Jugador(models.Model):
        
    
    POSICIONES = [
        ('POR', 'Portero'),
        ('DEF', 'Defensa'),
        ('MC', 'Medio campo'),
        ('DEL', 'Delantero'),
        ('SP', 'Sin posición'),
    ]
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    dorsal = models.PositiveSmallIntegerField()
    posicion = models.CharField(max_length=5, blank=False, null=False, choices=POSICIONES, default='SP')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='jugadores')
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"