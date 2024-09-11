
lista_compras = []  # Inicia lista vacia

while True:
    print("\nMenú principal:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Mostrar Lista")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == '1':   # Agregar artículo
            articulo = input("Nombre del articulo: ") 
            lista_compras.append(articulo)
            print(f"'{articulo}' agregado a la lista.")

    elif opcion == '2':  #Eliminar articulo
        if lista_compras:

            print("\nLista actual: ")
            for i, item in enumerate(lista_compras):
                print(f"{i + 1}. {item}")
            indice = int(input("Ingrese número del articulo a eliminar: ")) -1
            if 0 <= indice < len(lista_compras):
                eliminado = lista_compras.pop(indice)
                print(f"\ '{eliminado}' ha sido eliminado.")
            else:
                print("indice invalido.")

        else:
            print("la lista esta vacia.")

    elif opcion == '4':  #Salir del programa
         print("!Gracias por utilizar la lista de comprar! vuelve pronto putito.")
         break

    else:
         print("Opción no valida, elige una opción entre 1 y 4.")

         





