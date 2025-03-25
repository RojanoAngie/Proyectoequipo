if __name__ == '__main__':

    inventario = []
    while True:
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Vender producto")
        print("4. Salir")
        opcion = input("Elige una opción: ")


        if opcion == '1':
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad: "))
            existe = False
            for prod in inventario:
                if prod[0] == nombre:
                    prod[1] += cantidad
                    existe = True
                    break
            if existe == False:
                inventario.append([nombre, cantidad])


        if opcion == '2':
            for prod in inventario:
                print(prod[0], prod[1])


        if opcion == '3':
            nombre = input("Introduce el nombre del producto: ")
            for prod in inventario:
                if prod[0] == nombre:
                    if prod[1] > 0:
                        prod[1] -= 1
                        if prod[1] == 0:
                            inventario.remove(prod)
                    break


        if opcion == '4':
            break


        if opcion != '1' and opcion != '2' and opcion != '3' and opcion != '4':
            print("Opción no válida")
