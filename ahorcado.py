import random
import string

palabras = ['televisor', 'hola', 'moto', 'python',
            'estudio', 'ahorcado', 'auto', 'abeja', 'silla']


def ahorcado():

    print("=======================================")
    print("        WELCOME,GOOD LUCK  ;)          ")
    print("=======================================")
    palabra = random.choice(palabras)
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:

        print(
            f"Te quedan {vidas} vidas")

        palabra_lista = [
            letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input('Escoge una letra: ').lower()

        if letra_usuario in letras_por_adivinar:
            letras_adivinadas.add(letra_usuario)
            letras_por_adivinar.remove(letra_usuario)
            print('\n ¡¡¡¡VAMOS CARAJO ,ACERTASTE!!!!! SEGUI ASI!!!!')
        else:
            vidas = vidas - 1
            print(
                f'\n ¡¡¡ <{letra_usuario}>!!!!  NO ESTA EN LA PALABRA , TIENES QUE EZFORZARTE MAS.')

    if vidas == 0:
        print(
            f"¡AHORCADO! Perdiste. Lo lamento mucho. La palabra era: <{palabra}>")
    else:
        print(f'¡EXCELENTE! ¡Adivinaste la palabra ¡¡¡¡¡ <{palabra}>!!!!!!')


ahorcado()
