from django.shortcuts import render
from .models import PreguntaTrivia, OpcionTrivia
import random

def menu_principal(request):
    return render(request, 'interactiva/menu.html')

def inicio(request):
    return render(request, 'interactiva/inicio.html')

def trivias(request):
    respuesta = None
    pregunta = None

    if request.method == 'POST':
        opcion_id = request.POST.get('opcion')
        try:
            opcion = OpcionTrivia.objects.get(id=opcion_id)
            pregunta = opcion.pregunta  
            if opcion.es_correcta:
                respuesta = "¡Correcto! 🎉"
            else:
                respuesta = "Incorrecto 😞"
        except OpcionTrivia.DoesNotExist:
            respuesta = "Opción no válida."
    else:
        preguntas = PreguntaTrivia.objects.all()
        pregunta = random.choice(preguntas) if preguntas else None

    return render(request, 'interactiva/trivias.html', {
        'pregunta': pregunta,
        'respuesta': respuesta
    })


def votacion(request):
    return render(request, 'interactiva/votacion.html')

def encuestas(request):
    return render(request, 'interactiva/encuestas.html')

def programacion(request):
    return render(request, 'interactiva/programacion.html')
