if __name__ == '__main__':

    list=[]

    for i in range (20):
        list.append(i)

    inicio=1

    for i in range(1, 21):
        inicio= (inicio + i * 8 + 4) % i + 1
       # print(inicio)


    print("es hora de advinar el numero")
    n=int(input("ingrese su numero: "))

    while n != inicio:
        match n:
            case 1: print("el numero es mayor ");
            case 2: print("el numero es mayor ");
            case 3: print("el numero es mayor ");
            case 4: print("el numero es mayor ");
            case 5: print("el numero es mayor ");
            case 6: print("el numero es mayor ");
            case 8: print("el numero es menor");
            case 9: print("el numero es menor");
            case 10: print("el numero es menor");
            case 11: print("el numero es menor");
            case 12: print("el numero es menor");
            case 13: print("el numero es menor");
            case 14: print("el numero es menor");
            case 15: print("el numero es menor");
            case 16: print("el numero es menor");
            case 17: print("el numero es menor");
            case 18: print("el numero es menor");
            case 19: print("el numero es menor");
            case 20: print("el numero es menor");
            case _: print("fuera de rango");

        n = int(input("Ingresa tu número: "))

    print(f"este es el numero: {inicio}")