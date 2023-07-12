import random

def adivina_el_numero():
    print("Vamos a jugar!!")
    print("Tienes que adivinar un numero entre el 1 y el 100.")
    numero_seleccionado = random.randint(1, 100)
    
    while True:
        try:
            intento = int(input("Prueba: "))
            if intento < 1 or intento > 100:
                print("Tiene que ser un numero entre 1 y 100.")
                continue
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        if intento < numero_seleccionado:
            print("Error!! Es mayor que ", intento,". Inténtalo de nuevo!")
        elif intento > numero_seleccionado:
            print("Error!! Es menor que ", intento,". Inténtalo de nuevo!")
        else:
            print("Muy bien, la próxima será más difícil!")
            break

adivina_el_numero()
