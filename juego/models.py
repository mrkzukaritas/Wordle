from django.db import models
import random
class Palabras():
    words=["python",]
    cantidad= len(words)
    def palbraRandom(self):
        return self.words[random.randint(0,self.cantidad-1)]
# Create your models here.
class Game(models.Model):

    word_to_guess = Palabras().palbraRandom()
    historial= []
    attempts = models.IntegerField(default=0)
    max_attempts = models.IntegerField(default=6)
    is_won = models.BooleanField(default=False)

    def adivinar(self, palabra):
        self.attempts +=1
        if self.attempts >= self.max_attempts or self.is_won:
            return
        #crear un diccionario con una lista y llenarlo de ceros
        if palabra == self.word_to_guess:
            self.historial.append(palabra)
            self.is_won = True
            self.save()
            return
        adivinadas= []
        for char in palabra:
            adivinadas.append([char,0])


        cont=0
        for char in palabra:
            if char == self.word_to_guess[cont]:
                adivinadas[cont][1]=2
            elif char in self.word_to_guess:
                adivinadas[char][1]=1
            else:
                adivinadas[char][1]=0
            cont+=1

        self.save()
        self.historial.append( adivinadas)
        return 

