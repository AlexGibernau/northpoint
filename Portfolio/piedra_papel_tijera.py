import random

def piedra_papel_o_tijera():
    
    print("Vamos a jugar a piedra papel o tijera!")
    

    opciones = str["piedra","papel","tijera"]
    
    opcion = random.choice(opciones)

    mano = str(input("Que has sacado?"))

    if mano == "piedra" & opcion == "papel":
        print("he ganado! Buen intento")
    elif mano == "piedra" & opcion == "piedra":
        print("Empate... Te has salvado!")
    else:
        print("He perdido :(. La proxima te ganare!!")
piedra_papel_o_tijera()