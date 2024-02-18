from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    fecha_estreno = models.PositiveIntegerField()
    director = models.CharField(max_length=255)
    sinopsis = models.TextField()
# Nuevo campo para la cantidad de veces que la película ha sido vista
    mas_veces_vistas = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.titulo


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField()
    phone = models.CharField(max_length=13)
    age = models.IntegerField()
    pelicula_favorita = models.CharField(max_length=255, default='')

    ultima_pelicula_vista = models.CharField(max_length=255, default='')


    def __str__(self):
        return self.first_name+" "+self.last_name+":"+str(self.age)
        
        

        
