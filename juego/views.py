from django.shortcuts import render
from .models import Game

# Create your views here.
def home(request):
    juego= Game.objects.create()
    print(juego.word_to_guess)
    juego.adivinar("hola")
    print(juego.attempts)
    print(juego.historial)
    print(juego.is_won)
    juego.adivinar("yython")
    print(juego.historial)
    print(juego.attempts)
    print(juego.is_won)
    return render(request, 'index.html', {'game': juego})

def adivinar(request):
    juego= Game.objects.last()
    if request.POST:
        palabra= request.POST.get('your_name')
        juego.adivinar(palabra)
        return render(request, 'adivinar.html', {'game': juego})

    return render(request, 'adivinar.html', {'game': juego})

    


