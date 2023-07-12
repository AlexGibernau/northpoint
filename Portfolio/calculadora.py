def calculadora():    
    print("Slececciona que operacion quieres hacer:")
    print("1. Sumar.")
    print("2. Restar.")
    print("3. Multiplicar.")
    print("4. Dividir.")

    opcion = input()

    if opcion == "1":
        numero_1 = input("Indica el primer numero:")
        numero_2 = input("Indica el segundo numero:")
        print("El resultado de la suma es: " + str(int(numero_1) + int(numero_2)))
    elif opcion == "2":
        numero_1 = input("Indica el primer numero:")
        numero_2 = input("Indica el segundo numero:")
        print("El resultado de la resta es: " + str(int(numero_1) - int(numero_2)))
    elif opcion == "3":
        numero_1 = input("Indica el primer numero:")
        numero_2 = input("Indica el segundo numero:")
        print("El resultado de la multiplicacion es: " + str(int(numero_1) * int(numero_2)))
    elif opcion == "4":
        numero_1 = input("Indica el primer numero:")
        numero_2 = input("Indica el segundo numero:")
        print("El resultado de la division es: " + str(int(numero_1) / int(numero_2)))
    else: print("no es una opcion valida")

calculadora()