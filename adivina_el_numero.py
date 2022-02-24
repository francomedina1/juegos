import random


def adivina(x):

    print(
        """     =====================================
                    WELCOME
     ===================================== 
Adivina el numero!!!!!!!!!!""")

    numero_aleatorio = random.randint(1, x)
    numero_player = 0

    while numero_player != numero_aleatorio:
        numero_player = int(input(f"ingresaa el numero entre 1 y {x}: "))
        if numero_player > numero_aleatorio:
            print("tu numero es muy grande,vuelve a intentar")
        elif numero_player < numero_aleatorio:
            print("tu numero es muy chico , vuelve a intentarlo")

    print('¡¡¡¡¡¡¡¡¡felicitaciones, lo adivinaste!!!!!!!! Has tenido mucha suerte!!!!!')


adivina(10)
