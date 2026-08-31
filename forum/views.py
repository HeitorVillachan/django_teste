from django.http import HttpResponse
from .models import Pergunta

def index(request):
    perguntas = Pergunta.objects.all()
    saida = "<br>".join([p.titulo for p in perguntas])
    return HttpResponse(saida)