from django.db import models


class PreguntaTrivia(models.Model):
    texto = models.CharField(max_length=255)

    def __str__(self):
        return self.texto

class OpcionTrivia(models.Model):
    pregunta = models.ForeignKey(PreguntaTrivia, related_name='opciones', on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class Voto(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    puntaje = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class PreguntaEncuesta(models.Model):
    texto = models.CharField(max_length=255)

    def __str__(self):
        return self.texto

class OpcionEncuesta(models.Model):
    pregunta = models.ForeignKey(PreguntaEncuesta, related_name='opciones', on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)

class RespuestaEncuesta(models.Model):
    pregunta = models.ForeignKey(PreguntaEncuesta, on_delete=models.CASCADE)
    opcion = models.ForeignKey(OpcionEncuesta, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


# Create your models here.
