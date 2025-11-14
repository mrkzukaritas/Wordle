from django.shortcuts import render
from .models import Game

# Create your views here.
def home(request):
    juego= Game.objects.create()
    
    return render(request, 'index.html', {'game': juego})

def adivinar(request):
    juego= Game.objects.last()
    if request.POST:
        palabra= request.POST.get('your_name')
        juego.adivinar(palabra)
        return render(request, 'adivinar.html', {'game': juego})

    return render(request, 'adivinar.html', {'game': juego})

    


