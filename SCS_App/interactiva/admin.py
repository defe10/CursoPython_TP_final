from django.contrib import admin

from .models import (
    PreguntaTrivia, OpcionTrivia,
    Pelicula, Voto,
    PreguntaEncuesta, OpcionEncuesta, RespuestaEncuesta
)

admin.site.register(PreguntaTrivia)
admin.site.register(OpcionTrivia)
admin.site.register(Pelicula)
admin.site.register(Voto)
admin.site.register(PreguntaEncuesta)
admin.site.register(OpcionEncuesta)
admin.site.register(RespuestaEncuesta)

# Register your models here.
