from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    ROLES = [
        ('Agricultor', 'Agricultor'),
        ('Comerciante', 'Comerciante'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefono = models.CharField(max_length=15, blank=True, null=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='Agricultor')
    ubicacion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username} - {self.rol}"

class Publicacion(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField()
    unidad = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='publicaciones/', blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.producto} - {self.vendedor.username}"

class VisitaPublicacion(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='visitas')
    comerciante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visitas')
    visitado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('publicacion', 'comerciante')  # Un comerciante solo se registra una vez por publicación

    def __str__(self):
        return f"{self.comerciante.username} vio {self.publicacion.producto}"